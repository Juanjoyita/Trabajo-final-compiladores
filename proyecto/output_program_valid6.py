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
    b = to_bool(True)
    c = to_bool(False)
    # --- IF ---
    if (((a and b)) or (not c)):
        print(str(a))  # print(a)
    # --- Fin del programa generado ---

if __name__ == '__main__':
    main()