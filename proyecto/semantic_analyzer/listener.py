from antlr4.error.ErrorListener import ErrorListener  # Importa clase base para listeners de errores de ANTLR

# ===============================================================
# LÉXICO: DETECTOR DE ERRORES LÉXICOS
# ===============================================================
class LexerErrorListener(ErrorListener):
    """
    Listener personalizado para errores léxicos.
    Se activa cuando el lexer detecta tokens inválidos o caracteres prohibidos.
    """

    def __init__(self):
        super().__init__()       # Llama al constructor de la clase base
        self.errors = []         # Lista para almacenar errores léxicos detectados

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Método que captura errores del lexer automáticamente.
        Parámetros:
        - recognizer: lexer que detectó el error
        - offendingSymbol: token problemático
        - line, column: posición del error
        - msg: mensaje de error
        """
        text = offendingSymbol.text if offendingSymbol else "?"  # Obtiene el texto del token

        # Intenta clasificar el error según el tipo de token
        try:
            token_type = offendingSymbol.type                 # Tipo de token
            token_names = recognizer.symbolicNames           # Nombres de tokens definidos en la gramática

            if token_type == token_names.index("INVALID_NUMBER"):
                # Error de número no permitido
                error_message = f"[Línea {line}, Columna {column}] Error léxico: Uso de números no permitido ('{text}')"
            elif token_type == token_names.index("ERROR_CHAR"):
                # Error de carácter inválido
                error_message = f"[Línea {line}, Columna {column}] Error léxico: Carácter no permitido ('{text}')"
            else:
                # Cualquier otro error genérico del lexer
                error_message = f"[Línea {line}, Columna {column}] Error léxico: {msg}"
        except Exception:
            # Si falla la identificación del tipo de token, usa mensaje genérico
            error_message = f"[Línea {line}, Columna {column}] Error léxico: {msg}"

        self.errors.append(error_message)  # Guarda el error en la lista

# ===============================================================
# SINTAXIS: DETECTOR DE ERRORES SINTÁCTICOS
# ===============================================================
class SyntaxErrorListener(ErrorListener):
    """
    Listener personalizado para errores sintácticos.
    Se activa cuando el parser encuentra estructuras inválidas:
      - Falta de ';'
      - Paréntesis o llaves mal colocados
      - Orden incorrecto de tokens
    """

    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base
        self.errors = []    # Lista para almacenar errores sintácticos

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Método que captura errores de sintaxis automáticamente.
        Parámetros:
        - recognizer: parser que detectó el error
        - offendingSymbol: token problemático
        - line, column: posición del error
        - msg: mensaje generado por ANTLR
        """
        text = offendingSymbol.text if offendingSymbol else "?"  # Texto del token problemático
        error_message = f"[Línea {line}, Columna {column}] Error sintáctico: {msg}"  # Crea mensaje detallado
        self.errors.append(error_message)  # Guarda el error en la lista
