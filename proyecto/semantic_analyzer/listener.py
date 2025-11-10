# semantic_analyzer/listener.py

from antlr4.error.ErrorListener import ErrorListener

class LexerErrorListener(ErrorListener):
    """Captura y almacena errores léxicos del lexer (caracteres no válidos)."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Este método se ejecuta cuando ANTLR detecta un error LÉXICO,
        por ejemplo: caracteres inválidos, tokens mal formados, etc.
        """
        error_message = f"[Línea {line}, Columna {column}] Error léxico: {msg}"
        self.errors.append(error_message)


class SyntaxErrorListener(ErrorListener):
    """Captura y almacena errores sintácticos del parser."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Este método se ejecuta cuando ANTLR detecta un error SINTÁCTICO,
        por ejemplo: falta de ';', paréntesis incorrectos, tokens fuera de lugar, etc.
        """
        error_message = f"[Línea {line}, Columna {column}] Error sintáctico: {msg}"
        self.errors.append(error_message)
