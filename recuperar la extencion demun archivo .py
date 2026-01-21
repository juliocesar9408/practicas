import os

ruta_archivo = r' C\User\laurentine.masson\
100_ejercicio_python.ipynb'

## obtener el nombre del archivo 100_ejercicios_python.ipynb
nombre_archivo = os.path.basename(ruta_archivo)
##comvertir el nombre del archivoen una lista y recuperar el ultimo
##elemnto de esta ñlista que recupera est a extencion.

extencion_archivo = nombre_archivo.split(".")[-1]
print("extencion archivo :", extencion_archivo)
