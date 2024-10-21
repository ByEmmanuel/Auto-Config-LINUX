#!/bin/bash

# Script para instalar Python en Arch Linux

# Actualizar la lista de paquetes y actualizar el sistema
echo "Actualizando el sistema..."
sudo pacman -Syu --noconfirm

# Verificar si Python ya está instalado
if command -v python3 &>/dev/null; then
    echo "Python ya está instalado. Versión actual:"
    python3 --version
else
    echo "Python no está instalado. Procediendo con la instalación..."

    # Instalar Python
    sudo pacman -S python --noconfirm

    # Verificar la instalación
    if command -v python3 &>/dev/null; then
        echo "Python se ha instalado correctamente. Versión:"
        python3 --version
    else
        echo "Hubo un error al instalar Python."
    fi
fi

# Mensaje final
echo "Script de instalación de Python completado."