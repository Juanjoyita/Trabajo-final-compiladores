from generated.LogicaVisitor import LogicaVisitor

class IRGenerator(LogicaVisitor):
    """
    Generador de IR (TAC - Three Address Code) para el mini compilador.

    Esta clase recorre el AST (árbol sintáctico) y construye código
    intermedio independiente del lenguaje final. El IR es útil para:

    - Optimización
    - Análisis de flujo de control
    - Traducción a otros lenguajes
    - Depuración del compilador

    Cada instrucción generada es tipo:
        t1 = A AND B
        if t1 goto L1
        x = t2
        L3:
    """

    def __init__(self):
        # Lista donde se guardan todas las instrucciones TAC
        self.instructions = []

        # Contadores para generar nombres temporales únicos
        self.temp_counter = 0

        # Contadores para generar etiquetas únicas
        self.label_counter = 0

    # ======================================================
    # Utilidades internas
    # ======================================================

    def new_temp(self):
        """
        Crea un nombre temporal nuevo.
        Se usa para almacenar resultados intermedios como:
            t1 = TRUE AND FALSE
        """
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def new_label(self):
        """
        Genera nombres de etiquetas para saltos (goto), como:
            L1:
            L2:
        """
        self.label_counter += 1
        return f"L{self.label_counter}"

    # ======================================================
    # Nodo raíz del programa
    # ======================================================

    def visitProgram(self, ctx):
        """
        Recorre todas las sentencias del programa.
        Un programa es simplemente una lista de statements.
        """
        for stmt in ctx.statement():
            self.visit(stmt)

        # Retornamos todas las instrucciones generadas
        return self.instructions

    # ======================================================
    # Asignación
    # ======================================================

    def visitAssignment(self, ctx):
        """
        Traduce:
            x = expresión
        a IR:
            t1 = (expresión evaluada)
            x = t1
        """
        var = ctx.ID().getText()            # Nombre de la variable
        expr = self.visit(ctx.boolExpr())   # IR de la expresión booleana
        self.instructions.append(f"{var} = {expr}")

    # ======================================================
    # PRINT
    # ======================================================

    def visitPrintStmt(self, ctx):
        """
        Genera TAC para imprimir una variable:
            print(x)
        Se traduce a:
            print x
        """
        var = ctx.ID().getText()
        self.instructions.append(f"print {var}")

    # ======================================================
    # IF / ELSE
    # ======================================================

    def visitIfStmt(self, ctx):
        """
        Traduce estructuras:
            if (cond) { then }
            else { else }

        Genera TAC:
            t1 = (condición)
            if t1 goto Ltrue
            (bloque else)
            goto Lend
        Ltrue:
            (bloque then)
        Lend:
        """

        # Generar IR de la condición
        cond = self.visit(ctx.boolExpr())

        # Crear etiquetas L1, L2
        label_true = self.new_label()
        label_end = self.new_label()

        # Salto si la condición se cumple
        self.instructions.append(f"if {cond} goto {label_true}")

        # ELSE opcional
        if ctx.block(1):
            self.visit(ctx.block(1))

        # Salto al final del if
        self.instructions.append(f"goto {label_end}")

        # Etiqueta del bloque THEN
        self.instructions.append(f"{label_true}:")

        # Visitar bloque THEN
        self.visit(ctx.block(0))

        # Fin del IF/ELSE
        self.instructions.append(f"{label_end}:")

    # ======================================================
    # WHILE
    # ======================================================

    def visitWhileStmt(self, ctx):
        """
        Traduce:
            while (cond) { body }

        A TAC:
        Lstart:
            if NOT cond goto Lend
            (body)
            goto Lstart
        Lend:
        """

        # Etiquetas de inicio y fin
        label_start = self.new_label()
        label_end = self.new_label()

        # Punto donde comienza el ciclo
        self.instructions.append(f"{label_start}:")

        # IR para la condición
        cond = self.visit(ctx.boolExpr())

        # Si NO se cumple la condición → salir del ciclo
        self.instructions.append(f"if not {cond} goto {label_end}")

        # Cuerpo del while
        self.visit(ctx.block())

        # Volver a evaluar la condición
        self.instructions.append(f"goto {label_start}")

        # Fin del ciclo
        self.instructions.append(f"{label_end}:")

    # ======================================================
    # Bloque
    # ======================================================

    def visitBlock(self, ctx):
        """
        Un bloque es una lista de statements:
            { stmt1; stmt2; stmt3; }
        Se visitan uno por uno.
        """
        for stmt in ctx.statement():
            self.visit(stmt)

    # ======================================================
    # Expresiones booleanas
    # ======================================================

    def visitOrExpr(self, ctx):
        """
        Traduce:
            A OR B
        A:
            t1 = (A)
            t2 = (B)
            t3 = t1 OR t2
        Retorna t3
        """
        left = self.visit(ctx.boolExpr())   # izquierda
        right = self.visit(ctx.boolTerm())  # derecha
        t = self.new_temp()
        self.instructions.append(f"{t} = {left} OR {right}")
        return t

    def visitAndExpr(self, ctx):
        """
        Traduce:
            A AND B
        A:
            t1 = (A)
            t2 = (B)
            t3 = t1 AND t2
        """
        left = self.visit(ctx.boolTerm())
        right = self.visit(ctx.boolFactor())
        t = self.new_temp()
        self.instructions.append(f"{t} = {left} AND {right}")
        return t

    def visitNotFactor(self, ctx):
        """
        Traduce:
            NOT A
        TAC:
            t1 = NOT A
        """
        val = self.visit(ctx.boolFactor())
        t = self.new_temp()
        self.instructions.append(f"{t} = NOT {val}")
        return t

    def visitParenExpr(self, ctx):
        """
        Expresión entre paréntesis: (expr)
        Se evalúa directamente sin generar código adicional.
        """
        return self.visit(ctx.boolExpr())

    def visitIdExpr(self, ctx):
        """
        Retorna el nombre de una variable:
            x
        """
        return ctx.ID().getText()

    def visitTrueExpr(self, ctx):
        """
        Constante TRUE → se usa tal cual.
        """
        return "TRUE"

    def visitFalseExpr(self, ctx):
        """
        Constante FALSE → se usa tal cual.
        """
        return "FALSE"
