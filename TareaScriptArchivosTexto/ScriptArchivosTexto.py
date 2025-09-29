"""
Trabajo con Archivos de Texto en Python
Archivo: trabajo_archivos_texto.py
Autor: Christian Estupiñán Quintero
Curso: 1º D de Tecnologías de la Información
Asignatura: Fundamentos de Programación
Descripción: Este script crea un archivo de notas llamado "my_notes.txt",
escribe varias líneas de notas personales en él y luego las lee línea por línea
mostrando su contenido en la consola.
"""

# ============================
# Escritura de Archivo de Texto
# ============================

with open("my_notes.txt", "w") as archivo:
    archivo.write("Nota 1: Recordar comprar frutas.\n")
    archivo.write("Nota 2: Estudiar Python todos los días.\n")
    archivo.write("Nota 3: Hacer ejercicio por la mañana.\n")

# ============================
# Lectura de Archivo de Texto
# ============================

with open("my_notes.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

# ============================
# Fin del script
# ============================
