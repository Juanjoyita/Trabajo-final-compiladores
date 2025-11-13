class SymbolTable:
    """
    Tabla de símbolos simple para el compilador.
    Controla qué variables han sido declaradas y su tipo (aquí siempre booleano).
    """

    def __init__(self):
        self.symbols = {}           # Diccionario para almacenar variables: {nombre_variable: tipo}

    def declare(self, name):
        self.symbols[name] = "bool" # Declara la variable y asigna su tipo como "bool"

    def exists(self, name):
        return name in self.symbols  # Retorna True si la variable ya está declarada, False si no

    def __repr__(self):
        return str(self.symbols)     # Representación en cadena de la tabla, útil para depuración
