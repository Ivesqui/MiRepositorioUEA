# ============================
# Escritura de Archivo de Texto con entrada manual
# ============================

nombre_archivo = "my_notes2.txt"

print("Bienvenido al gestor de notas.")
print("Escribe tus notas. Cuando quieras terminar, deja la entrada vacía y presiona Enter.\n")

with open(nombre_archivo, "w") as archivo:
    contador = 1
    while True:
        nota = input(f"Ingresa Nota {contador}: ")
        if nota.strip() == "":  # Si el usuario deja la entrada vacía, termina
            break
        archivo.write(f"Nota {contador}: {nota}\n")
        contador += 1

print(f"\nNotas guardadas exitosamente en '{nombre_archivo}'.")

# ============================
# Lectura de Archivo de Texto
# ============================

print("\nContenido del archivo:\n")
with open(nombre_archivo, "r") as archivo:
    for linea in archivo:
        print(linea.strip())

# ============================
# Fin del script
# ============================
