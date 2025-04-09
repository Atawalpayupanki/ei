import subprocess
import os
import sys

env_name = ".venv"


subprocess.run([sys.executable, "-m", "venv", env_name])
print(f"Entorno virtual '{env_name}' creado.")

activate_script = os.path.join(env_name, "Scripts", "activate")

subprocess.run([sys.executable, "-m", "venv", env_name])

with open(".venv/.gitignore", "w") as f:
    f.write(".venv")

repositorio= f"{input("Introduce el nombre del repositorio: ")}.git"
comandos = [
    ["git", "init"],
    ["git", "add", "."],
    ["git", "commit", "-m", "firchtcommit"],
    ["git", "branch", "-M", "main"],
    ["git", "remote", "add", "origin", f"https://github.com/Atawalpayupanki/ei.git"],
    # ["git", "push", "-u", "origin", "main"]
]
for comando in comandos:
    subprocess.run(comando, text=True)
