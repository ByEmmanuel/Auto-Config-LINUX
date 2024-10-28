import os
import platform
import subprocess

def abrir_terminal():
    sistema = platform.system()

    if sistema == "Darwin":  # macOS
        subprocess.run(["open", "-a", "Terminal"])
    elif sistema == "Windows":  # Windows
        subprocess.run("start", shell=True)
    elif sistema == "Linux":  # Linux
        terminal = os.getenv("TERM", "x-terminal-emulator")  # Intenta usar el terminal por defecto
        subprocess.run([terminal])
    else:
        print("Sistema operativo no reconocido.")

if __name__ == "__main__":
    abrir_terminal()