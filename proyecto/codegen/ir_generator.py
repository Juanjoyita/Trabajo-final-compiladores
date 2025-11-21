# Importamos el Visitor generado por ANTLR.
# Este Visitor permite recorrer el árbol sintáctico (AST) automáticamente.
from generated.LogicaVisitor import LogicaVisitor


class IRGenerator(LogicaVisitor):
    """
    ============================================================
    GENERADOR DE IR (INTERMEDIATE REPRESENTATION / TAC)
    ============================================================
    Este módulo convierte el árbol sintáctico (AST) generado por
    ANTLR en un conjunto de instrucciones simples conocidas como:

        • TAC = Three Address Code (código de tres direcciones)

    ¿Por qué existe el IR?
    -----------------------
    - Hace que el compilador sea más fácil de analizar.
    - Permite agregar optimizaciones en el futuro.
    - Facilita la traducción a código final (Python, C, Java...).
    - Permite depurar el programa paso a paso.

    ¿Cómo se ve el IR?
    -------------------
        t1 = TRUE AND FALSE
        if t1 goto L1
        x = t2
        L3:

    Este tipo de instrucciones es lo que generan los compiladores reales.
    """


    def __init__(self):
        """
        Constructor del generador IR.
        Aquí inicializamos las estructuras necesarias:
        - La lista de instrucciones IR.
        - Contadores para temporales y etiquetas.
        """
        # Lista que almacenará TODAS las instrucciones TAC generadas
        self.instructions = []

        # Contador de temporales: t1, t2, t3, ...
        self.temp_counter = 0

        # Contador de etiquetas: L1, L2, L3, ...
        self.label_counter = 0


    # ======================================================
    # MÉTODOS DE UTILIDAD INTERNA
    # ======================================================

    def new_temp(self):
        """
        Crea un nuevo registro temporal.
        Se usa para guardar resultados intermedios.
        Ejemplo: t1 = TRUE AND FALSE
        """
        self.temp_counter += 1
        return f"t{self.temp_counter}"


    def new_label(self):
        """
        Crea una nueva etiqueta para estructuras de control
        como IF y WHILE.
        Ejemplo: L1:
        """
        self.label_counter += 1
        return f"L{self.label_counter}"


    # ======================================================
    # REGLA PRINCIPAL DEL PROGRAMA
    # ======================================================

    def visitProgram(self, ctx):
        """
        Un programa es una lista de sentencias.
        Las recorremos una por una generando IR.
        """
        for stmt in ctx.statement():
            self.visit(stmt)

        # Retornamos TODAS las instrucciones generadas
        return self.instructions


    # ======================================================
    # ASIGNACIÓN: x = expresión booleana
    # ======================================================

    def visitAssignment(self, ctx):
        """
        Traduce una asignación.

        Ejemplo:
            x = TRUE AND FALSE;

        IR generado:
            t1 = TRUE AND FALSE
            x = t1
        """
        var = ctx.ID().getText()          # nombre de variable
        expr = self.visit(ctx.boolExpr()) # TAC de expresión booleana

        self.instructions.append(f"{var} = {expr}")


    # ======================================================
    # PRINT: print(x)
    # ======================================================

    def visitPrintStmt(self, ctx):
        """
        Genera TAC para imprimir una variable.

        print(x);

        IR:
            print x
        """
        var = ctx.ID().getText()
        self.instructions.append(f"print {var}")


    # ======================================================
    # IF / ELSE
    # ======================================================

    def visitIfStmt(self, ctx):
        """
        Traducción del IF/ELSE a TAC.

        Ejemplo:
            if (cond) { ... } else { ... }

        IR generado:

            t1 = (evaluación de condición)
            if t1 goto L1
            (bloque else)
            goto L2
        L1:
            (bloque then)
        L2:
        """

        cond = self.visit(ctx.boolExpr())  # TAC de la condición

        label_true = self.new_label()      # etiqueta para THEN
        label_end = self.new_label()       # etiqueta final

        # Si la condición es TRUE → saltar al THEN
        self.instructions.append(f"if {cond} goto {label_true}")

        # Si existe bloque ELSE, procesarlo aquí
        if ctx.block(1):
            self.visit(ctx.block(1))

        # Saltar al final del IF
        self.instructions.append(f"goto {label_end}")

        # Etiqueta de entrada al THEN
        self.instructions.append(f"{label_true}:")

        # Procesar el bloque THEN
        self.visit(ctx.block(0))

        # Fin del IF
        self.instructions.append(f"{label_end}:")


    # ======================================================
    # WHILE
    # ======================================================

    def visitWhileStmt(self, ctx):
        """
        Traducción del WHILE al IR.

        while (cond) { body }

        IR:

        Lstart:
            if not cond goto Lend
            (body)
            goto Lstart
        Lend:
        """

        label_start = self.new_label()  # inicio del ciclo
        label_end = self.new_label()    # salida del ciclo

        # Etiqueta inicial
        self.instructions.append(f"{label_start}:")

        # Evaluar condición
        cond = self.visit(ctx.boolExpr())

        # Si cond es FALSA → terminar ciclo
        self.instructions.append(f"if not {cond} goto {label_end}")

        # Procesar cuerpo del while
        self.visit(ctx.block())

        # Volver al inicio
        self.instructions.append(f"goto {label_start}")

        # Etiqueta de salida
        self.instructions.append(f"{label_end}:")


    # ======================================================
    # BLOQUE { ... }
    # ======================================================

    def visitBlock(self, ctx):
        """
        Un bloque es simplemente un conjunto de sentencias.
        Se visitan todas.
        """
        for stmt in ctx.statement():
            self.visit(stmt)


    # ======================================================
    # EXPRESIONES BOOLEANAS
    # ======================================================

    def visitOrExpr(self, ctx):
        """
        Traduce A OR B.

        IR:
            t1 = (A)
            t2 = (B)
            t3 = t1 OR t2
        """

        left = self.visit(ctx.boolExpr())
        right = self.visit(ctx.boolTerm())

        t = self.new_temp()
        self.instructions.append(f"{t} = {left} OR {right}")
        return t


    def visitAndExpr(self, ctx):
        """
        Traduce A AND B.

        IR:
            t1 = A
            t2 = B
            t3 = t1 AND t2
        """

        left = self.visit(ctx.boolTerm())
        right = self.visit(ctx.boolFactor())

        t = self.new_temp()
        self.instructions.append(f"{t} = {left} AND {right}")
        return t


    def visitNotFactor(self, ctx):
        """
        Traduce NOT A.

        IR:
            t1 = NOT A
        """
        val = self.visit(ctx.boolFactor())

        t = self.new_temp()
        self.instructions.append(f"{t} = NOT {val}")
        return t


    def visitParenExpr(self, ctx):
        """
        Si hay paréntesis, solo evaluamos lo de adentro.
        No se genera TAC extra.
        """
        return self.visit(ctx.boolExpr())


    def visitIdExpr(self, ctx):
        """
        Retorna el nombre de la variable tal cual.
        """
        return ctx.ID().getText()


    def visitTrueExpr(self, ctx):
        """
        Constante TRUE → se usa directamente.
        """
        return "TRUE"


    def visitFalseExpr(self, ctx):
        """
        Constante FALSE → se usa directamente.
        """
        return "FALSE"
