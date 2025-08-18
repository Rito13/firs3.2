import os
import re

# katalog z plikami fabryk
factory_dir = "src/industries"

# przeszukujemy wszystkie pliki .py w folderze
for filename in os.listdir(factory_dir):
    if filename.endswith(".py"):
        filepath = os.path.join(factory_dir, filename)
        with open(filepath, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            new_lines.append(line)
            # jeśli znajdziemy FIRS.enabled = True
            if re.match(r"\s*industry\.economy_variations\['FIRS'\]\.enabled\s*=\s*True", line):
                # wstawiamy LESSER_POLAND.enabled = True
                new_lines.append("industry.economy_variations['LESSER_POLAND'].enabled = True\n")

        with open(filepath, "w") as f:
            f.writelines(new_lines)

print("[OK] Wszystkie pliki zaktualizowane.")
