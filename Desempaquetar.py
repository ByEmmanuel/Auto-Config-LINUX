import os
import tarfile
import zipfile

def desempaquetar():
    # Ubicar la carpetta donde estan los archivos a descomprimir
    carpeta_descargas = os.path.expanduser("~/Downloads")
    
    # Listar archivos en la carpeta Downloads
    archivos = os.listdir(carpeta_descargas)
    archivos_comprimidos = [archivo for archivo in archivos if archivo.endswith(('.tar.gz', '.tar', '.tar.xz', '.zip'))]
    
    # Verificar si hay archivos comprimidos
    if not archivos_comprimidos:
        print(f"No hay archivos comprimidos en la carpeta {carpeta_descargas}")
        return
        
    # Mostrar los archivos comprimidos
    print("Archivos disponibles para desempaquetar:")
    for idx, archivo in enumerate(archivos_comprimidos):
        print(f"{idx + 1}. {archivo}")
    
    # Solicitar al usuario que elija el archivo a desempaquetar
    seleccion = int(input("Elige el número del archivo que deseas desempaquetar: ")) - 1
    print("Pulsa CTRL + C para cancelar.")
    archivo_seleccionado = archivos_comprimidos[seleccion]
    
    # Ruta completa del archivo seleccionado 
    ruta_archivo = os.path.join(carpeta_descargas, archivo_seleccionado)
   
    # Preguntar si el usuario quiere crear una carpeta nueva para ese archivo
    crear_carpeta = int(input("¿Quieres crear una carpeta nueva para el archivo? \n1: Sí \n2: No\n")) == 1
    carpeta_seleccionada = carpeta_descargas

    # Si elige crear una carpeta nueva
    if crear_carpeta == 1:
        carpeta_seleccionada = os.path.join(carpeta_descargas, f"{archivo_seleccionado}-des")
        os.makedirs(carpeta_seleccionada, exist_ok=True)
    
    # Desempaquetar el archivo
    try: 
        if ruta_archivo.endswith((".tar.gz", ".tar.xz", ".tar")): 
            with tarfile.open(ruta_archivo) as archivo_tar:  
                archivo_tar.extractall(carpeta_seleccionada) 
                print(f"Archivo '{archivo_seleccionado}' desempaquetado correctamente en '{carpeta_seleccionada}'") 
                
        elif ruta_archivo.endswith(".zip"):
            with zipfile.ZipFile(ruta_archivo, 'r') as archivo_zip: 
                archivo_zip.extractall(carpeta_seleccionada) 
                print(f"Archivo '{archivo_seleccionado}' desempaquetado correctamente en '{carpeta_seleccionada}'") 
                
    except Exception as e: 
        print(f"Error al desempaquetar el archivo: {e}")  
    
if __name__ == "__main__":
    desempaquetar() 

