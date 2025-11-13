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
    c = to_bool(a)
    d = to_bool((not b))
    e = to_bool((a and b))
    f = to_bool((((a or b)) and ((c or d))))
    print(str(a))  # print(a)
    print(str(b))  # print(b)
    print(str(c))  # print(c)
    print(str(d))  # print(d)
    print(str(e))  # print(e)
    print(str(f))  # print(f)
    # --- Fin del programa generado ---

if __name__ == '__main__':
    main()