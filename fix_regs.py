import re
import pathlib
import shutil

# Katalog z kodem źródłowym NML
SRC_DIR = pathlib.Path("generated")  # zmień na "generated" jeśli chcesz poprawiać wynik kompilacji

# Zakres problematycznych rejestrów
RESERVED_RANGE = range(243, 256)

# Utworzenie kopii zapasowej
backup_dir = SRC_DIR.parent / (SRC_DIR.name + "_backup")
if not backup_dir.exists():
    shutil.copytree(SRC_DIR, backup_dir)
    print(f"[OK] Kopia zapasowa zapisana w: {backup_dir}")

# Regex dopasowujący STORE_TEMP(...) i LOAD_TEMP(...) z numerem 243–255
pattern = re.compile(r"(STORE_TEMP|LOAD_TEMP)\s*\(\s*(\d{3})\s*\)")

# Przechodzimy po wszystkich plikach .nml
for file_path in SRC_DIR.rglob("*.nml"):
    text = file_path.read_text(encoding="utf-8")

    def replacer(match):
        instr, num_str = match.groups()
        num = int(num_str)
        if num in RESERVED_RANGE:
            new_num = num - 128
            return f"{instr}({new_num})"
        return match.group(0)

    new_text = pattern.sub(replacer, text)

    if text != new_text:
        file_path.write_text(new_text, encoding="utf-8")
        print(f"[OK] Poprawiono: {file_path}")

print("\n[ZAKOŃCZONE] Wszystkie pliki przeanalizowane.")

