import time

def buscar_letras(palabra, array_principal):
    columnas = [""] * len(palabra)  # Inicializar columnas vacías para cada letra de la palabra
    
    for i, letra in enumerate(palabra):  # Iterar por cada letra de la palabra
        for char in array_principal:  # Iterar por cada letra del array principal
            # Agregar la letra a la columna correspondiente
            columnas[i] += char + " "
            
            # Limpiar la consola para que se vea más claro (solo en algunas terminales)
            #os.system('')  # Usa 'cls' si estás en Windows

            # Imprimir las columnas en su estado actual
            for fila in zip(*[col.split() for col in columnas]):
                print(" ".join(fila))
                
            # Pausa para simular el efecto visual
            time.sleep(0.1)
            
            # Si encontramos la letra deseada, romper el bucle
            if char == letra:
                break

# Array principal con todas las letras
array_principal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Palabra a buscar
palabra = "HELLO"

# Llamada a la función
buscar_letras(palabra, array_principal)