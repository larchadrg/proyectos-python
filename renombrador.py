#renombrador.py
#El usuario ingresa la direccion de una carpeta
#Luego, renombra todos los archivos de la carpeta por númeron

import os

#Paso 1: Indicar la carpeta donde se encuentran los archivos a renombrar 

direccion = input("Ingrese la direccion de la carpeta donde se alojan los archivos: \n")
os.chdir(direccion)

#print(os.getcwd())
#direccion actual 

contador = 0

for f in os.listdir():
    
    #f es cada archivo encontrado en el directorio 
    
    #print(f)
    #imprime los nombres de los archivos (extension incluida)

    #print(os.path.splitext(f))
    #devuelve una tupla que contiene el nombre "nombre" y la extension ".algo"

    nombreArc, extensionArc = os.path.splitext(f) 
    #guarda cada parte de la tupla en una extension diferente

    nuevoNombre = str(contador).zfill(len(str(len(os.listdir())))) + extensionArc
    os.rename(f, nuevoNombre)
    contador = contador + 1

print("Realizado!")
