# Nombre: Christian Iván Estupiñan Quintero
# Curso: 1ºD Tecnologías de la información
# Tarea: Trabajando con Diccionarios en Python con entradas del usuario

print("=== Sistema de Información Personal ===\n")

# 1) Crear el diccionario 'informacion_personal' con datos ingresados por el usuario.
informacion_personal = {
    "nombre": input("👉 Ingresa tu nombre: "),
    "edad": int(input("👉 Ingresa tu edad: ")),
    "ciudad": input("👉 Ingresa tu ciudad actual: "),
    "profesion": input("👉 Ingresa tu profesión: ")
}

print("\n✅ Diccionario inicial creado:")
print(informacion_personal)
print("-" * 50)

# 2) Acceder a la clave "ciudad" y modificarla por otra ciudad
nueva_ciudad = input("🌆 Ingresa una nueva ciudad para actualizar tu información: ")
informacion_personal["ciudad"] = nueva_ciudad

print("Ciudad actualizada con éxito.")
print("-" * 50)

# 3) Actualizar la profesión
nueva_profesion = input("💼 Ingresa tu profesión actualizada: ")
informacion_personal["profesion"] = nueva_profesion

print("Profesión actualizada con éxito.")
print("-" * 50)

# 4) Verificar si existe la clave "telefono"
if "telefono" not in informacion_personal:
    telefono = input("📱 Ingresa tu número de teléfono: ")
    informacion_personal["telefono"] = telefono
    print("Número de teléfono agregado con éxito.")
else:
    print("La clave 'telefono' ya existe en el diccionario.")

print("-" * 50)

# 5) Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("🔴 La clave 'edad' fue eliminada porque no es necesaria.")
else:
    print("La clave 'edad' no existe; nada que eliminar.")

print("-" * 50)

# 6) Imprimir el diccionario final después de todas las operaciones
print("🎉 Diccionario final resultante:")
print(informacion_personal)
