# Ejemplo de arreglo 3D: [ciudad][día][semana]
# Supongamos 2 ciudades, 7 días por semana, 3 semanas
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

# Calcular promedio por ciudad y semana
for i, ciudad in enumerate(temperaturas):
    print(f"Promedios para {ciudades[i]}:")
    for s in range(len(semanas)):
        suma = 0
        for d in range(len(ciudad)):  # días
            suma += ciudad[d][s]
        promedio = suma / len(ciudad)
        print(f"  {semanas[s]}: {promedio:.2f}°C")
    print()
