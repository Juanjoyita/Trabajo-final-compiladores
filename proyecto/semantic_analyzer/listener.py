from antlr4.error.ErrorListener import ErrorListener

class LexerErrorListener(ErrorListener):
    """Captura y almacena errores léxicos del lexer (caracteres o tokens no válidos)."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        text = offendingSymbol.text if offendingSymbol else "?"
        if offendingSymbol.type == recognizer.symbolicNames.index("INVALID_NUMBER"):
            error_message = f"[Línea {line}, Columna {column}] Error léxico: Uso de números no permitido ('{text}')"
        elif offendingSymbol.type == recognizer.symbolicNames.index("ERROR_CHAR"):
            error_message = f"[Línea {line}, Columna {column}] Error léxico: Carácter no permitido ('{text}')"
        else:
            error_message = f"[Línea {line}, Columna {column}] Error léxico: {msg}"
        self.errors.append(error_message)


class SyntaxErrorListener(ErrorListener):
    """Captura y almacena errores sintácticos del parser."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"[Línea {line}, Columna {column}] Error sintáctico: {msg}"
        self.errors.append(error_message)
