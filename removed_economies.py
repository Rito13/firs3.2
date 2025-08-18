import os
import re

industries_dir = 'src/industries'
removed_economies = ['BASIC_ARCTIC', 'BASIC_TEMPERATE', 'BASIC_TROPIC', 'STEELTOWN', 'MISTAH_KURTZ']

# regex dopasowujący linie zaczynające się od dowolnej ilości spacji, potem industry.economy_variations['...']
pattern = re.compile(rf"^\s*(industry\.economy_variations\['({'|'.join(removed_economies)})'\])")

for filename in os.listdir(industries_dir):
    if filename.endswith('.py'):
        filepath = os.path.join(industries_dir, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()

        changed = False
        with open(filepath, 'w') as f:
            for line in lines:
                if pattern.match(line) and not line.strip().startswith('#'):
                    line = '# ' + line
                    changed = True
                f.write(line)
        if changed:
            print(f"Zmodyfikowano: {filename}")

print("Gotowe. Wszystkie linie odwołujące się do usuniętych ekonomii zostały zakomentowane.")
