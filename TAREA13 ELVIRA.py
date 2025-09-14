# Datos de temperaturas de 4 ciudades, 4 semanas, 7 días cada semana
temperaturas = [
    [  # Ciudad 1
        [78, 80, 79, 77, 81, 82, 80],  # Semana 1
        [79, 81, 78, 80, 82, 83, 81],  # Semana 2
        [77, 78, 79, 80, 78, 79, 80],  # Semana 3
        [80, 81, 82, 79, 78, 80, 81]  # Semana 4
    ],
    [  # Ciudad 2
        [70, 72, 71, 73, 74, 72, 71],
        [71, 73, 70, 72, 74, 73, 72],
        [70, 71, 72, 73, 72, 71, 70],
        [72, 73, 74, 72, 71, 72, 73]
    ],
    [  # Ciudad 3
        [85, 84, 86, 87, 85, 86, 87],
        [86, 85, 84, 86, 87, 88, 85],
        [87, 86, 85, 86, 87, 86, 85],
        [85, 86, 87, 88, 86, 87, 85]
    ],
    [  # Ciudad 4
        [60, 62, 61, 63, 64, 62, 61],
        [61, 63, 60, 62, 64, 63, 62],
        [60, 61, 62, 63, 62, 61, 60],
        [62, 63, 64, 62, 61, 62, 63]
    ]
]


def promedio_por_ciudad(datos):
    """
    Calcula la temperatura promedio de cada ciudad.

    Parámetros:
    datos: lista 3D -> [ciudad][semana][día]

    Retorna:
    lista con los promedios por ciudad
    """
    promedios = []

    for ciudad in datos:
        suma_ciudad = 0
        dias_totales = 0
        for semana in ciudad:
            suma_ciudad += sum(semana)
            dias_totales += len(semana)
        promedio_ciudad = suma_ciudad / dias_totales
        promedios.append(promedio_ciudad)

    return promedios


# Calcular los promedios
promedios_ciudades = promedio_por_ciudad(temperaturas)

# Mostrar resultados
for i, promedio in enumerate(promedios_ciudades, start=1):
    print(f"Ciudad {i}: {promedio:.2f}°F")

    # Lista 3D de temperaturas: [ciudad][semana][día]
    temperaturas = [
        [[78, 80, 79, 77, 81, 82, 80], [79, 81, 78, 80, 82, 83, 81], [77, 78, 79, 80, 78, 79, 80],
         [80, 81, 82, 79, 78, 80, 81]],
        [[70, 72, 71, 73, 74, 72, 71], [71, 73, 70, 72, 74, 73, 72], [70, 71, 72, 73, 72, 71, 70],
         [72, 73, 74, 72, 71, 72, 73]],
        [[85, 84, 86, 87, 85, 86, 87], [86, 85, 84, 86, 87, 88, 85], [87, 86, 85, 86, 87, 86, 85],
         [85, 86, 87, 88, 86, 87, 85]],
        [[60, 62, 61, 63, 64, 62, 61], [61, 63, 60, 62, 64, 63, 62], [60, 61, 62, 63, 62, 61, 60],
         [62, 63, 64, 62, 61, 62, 63]]
    ]


    def promedio_por_ciudad(datos):
        """
        Calcula la temperatura promedio de cada ciudad.

        Parámetros:
        datos: lista 3D -> [ciudad][semana][día]

        Retorna:
        lista con los promedios por ciudad
        """
        promedios = []

        for ciudad in datos:
            suma_ciudad = 0
            dias_totales = 0
            for semana in ciudad:
                suma_ciudad += sum(semana)  # Sumar todas las temperaturas de la semana
                dias_totales += len(semana)  # Contar cuántos días tiene la semana
            promedio_ciudad = suma_ciudad / dias_totales
            promedios.append(promedio_ciudad)

        return promedios


    # Calcular y mostrar los promedios
    promedios_ciudades = promedio_por_ciudad(temperaturas)
    for i, promedio in enumerate(promedios_ciudades, start=1):
        print(f"Ciudad {i}: {promedio:.2f}°F")