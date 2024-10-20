import subprocess
import os

def ejecutar_comando(comando, descripcion):
    print(f"Iniciando: {descripcion}")
    resultado = subprocess.run(comando, shell=True)
    if resultado.returncode != 0:
        print(f"Error al ejecutar: {comando}")
    else:
        print(f"Completado: {descripcion}\n")

# Crear la carpeta 'workspace' en el directorio del usuario
def crear_carpeta_workspace():
    ruta_workspace = os.path.expanduser("~/workspace")  # Cambiado de ~/Home/workspace a ~/workspace
    if not os.path.exists(ruta_workspace):
        os.makedirs(ruta_workspace)
        print(f"Carpeta creada: {ruta_workspace}")
    else:
        print(f"La carpeta '{ruta_workspace}' ya existe.")

# Crear la carpeta workspace
crear_carpeta_workspace()

# Instalar yay y pip
ejecutar_comando("sudo pacman -S python-pip", "Instalando pip-Python")
ejecutar_comando("sudo pacman -S git base-devel", "Instalando yay")
#ejecutar_comando("git clone https://aur.archlinux.org/yay.git", "Instalando yay.")
#ejecutar_comando("cd yay", "Instalando yay..")
#ejecutar_comando("makepkg -si", "Instalando yay...")





# Instalar Neofetch
ejecutar_comando("sudo pacman -S neofetch", "Instalación de Neofetch")  # En Ubuntu usa: sudo apt install neofetch

# Instalar Git
ejecutar_comando("sudo pacman -S git", "Instalación de Git")  # En Ubuntu usa: sudo apt install git

nombre_git = input("Introduce tu nombre para la configuración de Git: ")
email_git = input("Introduce tu email para la configuración de Git: ")

# Configurar Git con las credenciales ingresadas
#ejecutar_comando(f"git config --global user.name '{nombre_git}'", "Configuración de Git (Nombre)")
#ejecutar_comando(f"git config --global user.email '{email_git}'", "Configuración de Git (Email)")

# Instalacion De Acpi
ejecutar_comando("sudo pacman -S acpi", "Instalando Acpi")

# Instalar htop
ejecutar_comando("sudo pacman -S htop", "Instalando htop")

# Instalar MariaDB
ejecutar_comando("sudo pacman -S mariadb", "Instalación de MariaDB")  # En Ubuntu usa: sudo apt install mariadb-server

# Inicializar MariaDB
ejecutar_comando("sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql", "Inicialización de MariaDB")


# Función para generar clave SSH
def generar_clave_ssh():
    ruta_ssh = os.path.expanduser("~/.ssh")
    
    # Crear directorio .ssh si no existe
    if not os.path.exists(ruta_ssh):
        os.makedirs(ruta_ssh)
        print(f"Carpeta .ssh creada en {ruta_ssh}")
    
    # Ruta de la clave SSH
    ruta_clave = os.path.join(ruta_ssh, "id_ed25519")
    
    # Verificar si la clave ya existe
    if os.path.exists(ruta_clave):
        print(f"La clave SSH ya existe en {ruta_clave}")
    else:
        email_ssh = input("Introduce tu email para la clave SSH: ")
        comando_generar_clave = f'ssh-keygen -t ed25519 -C "{email_ssh}" -f {ruta_clave} -N ""'
        ejecutar_comando(comando_generar_clave, "Generación de clave SSH")
        print(f"Clave SSH generada en {ruta_clave}")

# Preguntar si se desea instalar SSH
bandera_2_ = 1
while bandera_2_ == 1:
    print("\n¿Deseas Instalar SSH?\n 1 : SI \n 2 : NO")
    try:
        opcion = int(input())

        if opcion != 1 and opcion != 2:
            print("Error, Opción Inválida")
        elif opcion == 1:
            # Instalar OpenSSH
            def instalar_ssh():
                print("Instalando OpenSSH...")  # Aquí va tu lógica de instalación
                ejecutar_comando("sudo pacman -S openssh", "Instalación de OpenSSH")  # En Ubuntu usa: sudo apt install openssh-server
            instalar_ssh()
            generar_clave_ssh()
            bandera_2_ = 0
        elif opcion == 2:
            print("No se instalará SSH.")
            bandera_2_ = 0

    except ValueError:
        print("Error: Debes introducir un número válido.")

# Preguntar si se desea instalar DOCKER
bandera_3_ = 1

while bandera_3_ == 1:
    print("\n¿Deseas Instalar DOCKER?\n 1 : SI \n 2 : NO")
    try:
        opcion = int(input())

        if opcion != 1 and opcion != 2:
            print("Error, Opción Inválida")
        elif opcion == 1:
            # Instalar OpenSSH
            def instalar_ssh():
                print("Instalando DOCKER...")  # Aquí va tu lógica de instalación
                ejecutar_comando("sudo pacman -S docker", "Instalación de Docker")  # En Ubuntu usa: sudo apt install openssh-server
                ejecutar_comando("sudo systemctl start docker", "Iniciando Docker")
                ejecutar_comando("sudo systemctl enable docker", "Iniciando Docker Al iniciar")
                ejecutar_comando("sudo docker --version", ": <-- Version de docker <--")
                
            bandera_3_ = 0
        elif opcion == 2:
            print("No se instalará Docker.")
            bandera_3_ = 0

    except ValueError:
        print("Error: Debes introducir un número válido.")

print("\nDeseas instalar Entornos de desarrollo Integrados (IDE) para programar? ")
opcion_2_ = int(input("1: para visual studio code\n 2: para IntelliJ\n 3: para ambos"))
if opcion_2_ == 1:
    ejecutar_comando("yay -S visual-studio-code-bin",)
print()
print()

print("\nTodos los procesos completados correctamente.")
print("\nOpciones Finales : \n Comprobar el estado de docker en el sistema: 'sudo docker run hello-world'")
print("\n")