import os
import subprocess

TEST_FOLDER = "tests"
MAIN_FILE = "main.py"

def run_test(test_file):
    print(f"\n==============================")
    print(f" Ejecutando: {test_file}")
    print(f"==============================")

    result = subprocess.run(
        ["python3", MAIN_FILE, os.path.join(TEST_FOLDER, test_file)],
        capture_output=True,
        text=True
    )

    # Mostrar SOLO si hubo errores o si pasó correctamente
    if result.stdout.strip():
        print(result.stdout.strip())
    if result.stderr.strip():
        print("ERROR (stderr):")
        print(result.stderr.strip())


def main():
    # Listar todos los archivos .txt en /tests
    test_files = sorted([f for f in os.listdir(TEST_FOLDER) if f.endswith(".txt")])

    if not test_files:
        print("⚠ No hay archivos .txt en la carpeta tests/")
        return

    print("===== EJECUTANDO TODOS LOS TESTS =====")

    for tf in test_files:
        run_test(tf)

    print("\n===== FINALIZADO =====")


if __name__ == "__main__":
    main()
