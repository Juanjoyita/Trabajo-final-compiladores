# ============================================
# Código generado automáticamente por MiniCompilador
# NO MODIFICAR MANUALMENTE
# ============================================

def to_bool(value):
    """Convierte expresiones a booleano explícito."""
    return True if value is True else False

def main():
    # --- Inicio del programa generado ---
    a = to_bool(True)
    b = to_bool(False)
    # --- IF ---
    if (a and (not b)):
        print(str(a))  # print(a)
    else:
        print(str(b))  # print(b)
    # --- WHILE ---
    while a:
        a = to_bool(False)
    # --- Fin del programa generado ---

if __name__ == '__main__':
    main()