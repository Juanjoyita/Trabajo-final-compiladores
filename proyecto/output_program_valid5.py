# ============================================
# Código generado automáticamente por MiniCompilador
# NO MODIFICAR MANUALMENTE
# ============================================

def to_bool(value):
    """Convierte expresiones a booleano explícito."""
    return True if value is True else False

def main():
    # --- Inicio del programa generado ---
    x = to_bool(True)
    y = to_bool(False)
    # --- WHILE ---
    while x:
        print(str(x))  # print(x)
        x = to_bool(False)
    # --- Fin del programa generado ---

if __name__ == '__main__':
    main()