from antlr4.error.ErrorListener import ErrorListener


# ===============================================================
# LÉXICO: DETECTOR DE ERRORES LÉXICOS
# ===============================================================
class LexerErrorListener(ErrorListener):
    """
    Captura errores léxicos del lexer.
    Se activa cuando aparecen caracteres o tokens no válidos.
    """

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Detecta tipos de errores léxicos específicos:
        - Números no permitidos (token INVALID_NUMBER)
        - Caracteres desconocidos (token ERROR_CHAR)
        - Cualquier otro error genérico del lexer
        """
        text = offendingSymbol.text if offendingSymbol else "?"

        # Intentar identificar el tipo de token (según el índice del lexer)
        try:
            token_type = offendingSymbol.type
            token_names = recognizer.symbolicNames

            if token_type == token_names.index("INVALID_NUMBER"):
                error_message = f"[Línea {line}, Columna {column}] Error léxico: Uso de números no permitido ('{text}')"
            elif token_type == token_names.index("ERROR_CHAR"):
                error_message = f"[Línea {line}, Columna {column}] Error léxico: Carácter no permitido ('{text}')"
            else:
                error_message = f"[Línea {line}, Columna {column}] Error léxico: {msg}"
        except Exception:
            # Si por alguna razón no se puede identificar el tipo exacto
            error_message = f"[Línea {line}, Columna {column}] Error léxico: {msg}"

        self.errors.append(error_message)


# ===============================================================
# SINTAXIS: DETECTOR DE ERRORES SINTÁCTICOS
# ===============================================================
class SyntaxErrorListener(ErrorListener):
    """
    Captura errores sintácticos del parser.
    Se activa cuando hay estructuras inválidas en el lenguaje,
    como:
      - Falta de ';'
      - Paréntesis o llaves mal colocados
      - Tokens en orden incorrecto
    """

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Guarda el mensaje de error sintáctico.
        ANTLR provee automáticamente la descripción del fallo.
        """
        text = offendingSymbol.text if offendingSymbol else "?"
        error_message = f"[Línea {line}, Columna {column}] Error sintáctico: {msg}"
        self.errors.append(error_message)
