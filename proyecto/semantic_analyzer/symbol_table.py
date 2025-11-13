class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, name):
        self.symbols[name] = "bool"

    def exists(self, name):
        return name in self.symbols

    def __repr__(self):
        return str(self.symbols)