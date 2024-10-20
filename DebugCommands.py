def ejecutar_comando(instruccion, mensaje):
    print(instruccion, mensaje, 0)
    

bandera = 1

while bandera == 1:
    print("¿Deseas Instalar SSH?\n 1 : SI \n 2 : NO")
    try:
        opcion = int(input())

        if opcion != 1 and opcion != 2:
            print("Error, Opción Inválida")
        elif opcion == 1:
            # Instalar OpenSSH
            def instalar_ssh():
                print("Instalando OpenSSH...")  # Aquí va tu lógica de instalación
                ejecutar_comando("sudo pacman -S openssh", "Instalación de OpenSSH")
            instalar_ssh()
            bandera = 0
        elif opcion == 2:
            print("No se instalará SSH.")
            bandera = 0

    except ValueError:
        print("Error: Debes introducir un número válido.")

print("Todos los procesos han sido terminados")
