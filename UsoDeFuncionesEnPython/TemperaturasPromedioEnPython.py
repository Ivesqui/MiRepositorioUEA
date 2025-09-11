"""Nombre: Christian Iván Estupiñan Quintero
Curso: 1ºD Tecnologías de la Información

Tarea Individual: Desarrollo de Función para Calcular Temperaturas Promedio en Python
Objetivo: Practicar la definición y uso de funciones en Python
para calcular temperaturas promedio y utilizar la plataforma GitHub
para compartir el desarrollo de código. En esta tarea, utilizarás
los datos de temperaturas de clases anteriores.
Instrucciones:

Desarrollo de la Función:
Desarrolla una función en Python que calcule la temperatura
promedio de una ciudad durante un período de tiempo. La función
debe ser capaz de manejar datos de temperaturas de múltiples
ciudades y semanas.

Utiliza como base el ejemplo anterior, donde tenías datos de 3
ciudades durante 4 semanas.

Tu función debe recibir estos datos como parámetros y calcular
la temperatura promedio de cada ciudad."""

#Desarrollo:

# Datos de ejemplo
temperaturas = [
    [  # Ciudad 1
        [25, 26, 24],  # Lunes de cada semana
        [26, 27, 25],  # Martes
        [24, 26, 24],  # Miércoles
        [23, 25, 22],  # Jueves
        [25, 27, 24],  # Viernes
        [26, 28, 25],  # Sábado
        [27, 29, 26]   # Domingo
    ],
    [  # Ciudad 2
        [30, 31, 29],
        [31, 32, 30],
        [29, 30, 28],
        [28, 29, 27],
        [30, 31, 29],
        [31, 32, 30],
        [32, 33, 31]
    ]
]

ciudades = ["Ciudad 1", "Ciudad 2"]
semanas = ["Semana 1", "Semana 2", "Semana 3"]

# Función para calcular promedio de temperaturas
def calcular_promedio_temperaturas(datos, nombres_ciudades, nombres_semanas):
    """
    Calcula la temperatura promedio por ciudad y por semana.

    Parámetros:
    - datos: lista 3D [ciudad][día][semana]
    - nombres_ciudades: lista con los nombres de las ciudades
    - nombres_semanas: lista con los nombres de las semanas
    """
    for i, ciudad in enumerate(datos):
        print(f"Promedios para {nombres_ciudades[i]}:")
        for s in range(len(nombres_semanas)):
            suma = sum(ciudad[d][s] for d in range(len(ciudad)))  # sumar días de la semana s
            promedio = suma / len(ciudad)
            print(f"  {nombres_semanas[s]}: {promedio:.2f}°C")
        print()

# Llamar a la función
calcular_promedio_temperaturas(temperaturas, ciudades, semanas)
