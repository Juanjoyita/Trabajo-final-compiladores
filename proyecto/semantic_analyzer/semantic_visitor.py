from generated.LogicaVisitor import LogicaVisitor   # Importa la clase base Visitor generada por ANTLR
from generated.LogicaParser import LogicaParser     # Importa parser generado por ANTLR
from .symbol_table import SymbolTable              # Importa tabla de símbolos para seguimiento de variables

# ===============================================================
# ANALIZADOR SEMÁNTICO
# ===============================================================
class SemanticAnalyzer(LogicaVisitor):
    """
    Implementa el visitor para recorrer el árbol sintáctico (AST)
    y verificar reglas semánticas:
      - Variables declaradas antes de usar
      - Tipos booleanos en expresiones
      - Validez de bloques y condiciones
    """

    def __init__(self):
        self.symbols = SymbolTable()  # Inicializa la tabla de símbolos (variables declaradas)
        self.errors = []              # Lista para almacenar errores semánticos

    # -----------------------
    # VISITAR PROGRAMA COMPLETO
    # -----------------------
    def visitProgram(self, ctx):
        ok = True                          # Bandera para saber si todo es correcto
        for stmt in ctx.statement():       # Recorre todas las sentencias del programa
            if not self.visit(stmt):       # Visita cada sentencia usando el visitor
                ok = False                 # Si alguna falla, marca como falso
        return ok                          # Retorna True si todo es correcto, False si hay errores

    # -----------------------
    # VISITAR BLOQUE DE SENTENCIAS { ... }
    # -----------------------
    def visitBlock(self, ctx):
        ok = True
        for stmt in ctx.statement():       # Recorre sentencias dentro del bloque
            if not self.visit(stmt):       # Aplica visitor a cada sentencia
                ok = False
        return ok

    # -----------------------
    # VISITAR ASIGNACIÓN: ID = boolExpr;
    # -----------------------
    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()      # Obtiene nombre de la variable
        expr_ok = self.visit(ctx.boolExpr())  # Valida la expresión booleana asignada

        if not self.symbols.exists(var_name):  # Si variable no está declarada
            self.symbols.declare(var_name)    # La declara automáticamente

        return expr_ok                     # Retorna si la expresión es válida

    # -----------------------
    # VISITAR PRINT
    # -----------------------
    def visitPrintStmt(self, ctx):
        name = ctx.ID().getText()          # Obtiene la variable a imprimir

        if not self.symbols.exists(name):  # Verifica si la variable existe
            self.errors.append(f"[Error] Variable '{name}' no declarada antes de print().")
            return False                   # Error semántico si no existe

        return True                        # Variable correcta

    # -----------------------
    # VISITAR IF
    # -----------------------
    def visitIfStmt(self, ctx):
        cond_ok = self.visit(ctx.boolExpr())   # Valida la condición del if
        then_ok = self.visit(ctx.block(0))     # Valida el bloque del THEN
        else_ok = True

        if ctx.block(1):                        # Si existe ELSE
            else_ok = self.visit(ctx.block(1))  # Valida el bloque del ELSE

        return cond_ok and then_ok and else_ok  # Solo True si todo es válido

    # -----------------------
    # VISITAR WHILE
    # -----------------------
    def visitWhileStmt(self, ctx):
        cond_ok = self.visit(ctx.boolExpr())   # Valida condición del while
        body_ok = self.visit(ctx.block())      # Valida bloque del cuerpo
        return cond_ok and body_ok             # Retorna True si todo es válido

    # -----------------------
    # VISITAR EXPRESIONES BOOLEANAS
    # -----------------------
    def visitOrExpr(self, ctx):
        # Valida la expresión OR: expr OR term
        return self.visit(ctx.boolExpr()) and self.visit(ctx.boolTerm())

    def visitAndExpr(self, ctx):
        # Valida la expresión AND: term AND factor
        return self.visit(ctx.boolTerm()) and self.visit(ctx.boolFactor())

    def visitNotFactor(self, ctx):
        # Valida NOT factor
        return self.visit(ctx.boolFactor())

    def visitParenExpr(self, ctx):
        # Valida expresión entre paréntesis
        return self.visit(ctx.boolExpr())

    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()            # Obtiene el nombre de la variable

        if not self.symbols.exists(name):   # Verifica si está declarada
            self.errors.append(f"[Error] Variable '{name}' usada sin declarar.")
            return False

        return True

    def visitTrueExpr(self, ctx):
        # TRUE siempre válido
        return True

    def visitFalseExpr(self, ctx):
        # FALSE siempre válido
        return True
