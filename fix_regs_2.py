
import re
import os
import shutil

# Katalogi, które chcemy przeszukać
TARGET_DIRS = ["src", "generated"]

# Backup
BACKUP_DIR = "src_backup"
if not os.path.exists(BACKUP_DIR):
    shutil.copytree("src", BACKUP_DIR)
    print(f"[OK] Kopia zapasowa zapisana w: {BACKUP_DIR}")

# Wzorce do znajdowania liczb w STORE_TEMP i LOAD_TEMP
pattern = re.compile(r"(STORE_TEMP\s*\([^,]+,\s*|LOAD_TEMP\s*\()\s*(\d{3})")

def fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    def repl(match):
        prefix, num_str = match.groups()
        num = int(num_str)
        if 128 <= num <= 255:
            return f"{prefix}{num - 128}"
        return match.group(0)

    new_content = re.sub(pattern, repl, content)

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

changed_files = 0
for target_dir in TARGET_DIRS:
    if os.path.exists(target_dir):
        for root, dirs, files in os.walk(target_dir):
            for file in files:
                if file.endswith((".nml", ".pynml", ".txt")):
                    if fix_file(os.path.join(root, file)):
                        changed_files += 1

print(f"[ZAKOŃCZONE] Poprawiono pliki: {changed_files}")
