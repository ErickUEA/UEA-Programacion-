# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
# datos obtenidos de: https://shre.ink/rTgW
def calcular_temperatura_promedio(ciudades, temperaturas):

    promedios_ciudades = []  # Lista para almacenar los promedios de temperatura por ciudad

    # Recorremos la lista de temperaturas
    for ciudad_temperaturas in temperaturas:
        promedios_semana = []  # Lista para almacenar los promedios de temperatura por semana

        # Recorremos las temperaturas por semana
        for semana_temperaturas in ciudad_temperaturas:
            temps = semana_temperaturas[1::2]  # Obtener las temperaturas
            promedio_temp_semana = sum(temps) / len(temps)  # Calcular el promedio de temperatura por semana
            promedios_semana.append(promedio_temp_semana)

        promedio_temp_ciudad = sum(promedios_semana) / len(promedios_semana)  # Calcular el promedio de temperatura por ciudad
        promedios_ciudades.append(promedio_temp_ciudad)

    return promedios_ciudades


ciudades = ["Ambato", "Tena"]
temperaturas = [
    [
        ["Lunes", 24, "Martes", 26, "Miércoles", 25, "Jueves", 23, "Viernes", 24, "Sábado", 25, "Domingo", 26],
        ["Lunes", 26, "Martes", 27, "Miércoles", 27, "Jueves", 31, "Viernes", 28, "Sábado", 16, "Domingo", 16],
        ["Lunes", 29, "Martes", 31, "Miércoles", 29, "Jueves", 29, "Viernes", 31, "Sábado", 29, "Domingo", 26]
    ],
    [
        ["Lunes", 29, "Martes",  31, "Miércoles", 29, "Jueves", 28, "Viernes", 27, "Sábado", 30, "Domingo", 31],
        ["Lunes", 30, "Martes", 32, "Miércoles", 31, "Jueves", 30, "Viernes", 29, "Sábado", 29, "Domingo", 30],
        ["Lunes", 31, "Martes",  29, "Miércoles", 30, "Jueves", 29, "Viernes", 30, "Sábado", 32, "Domingo", 28]
    ]
]

promedios = calcular_temperatura_promedio(ciudades, temperaturas)

# Mostramos los resultados
for i, ciudad in enumerate(ciudades):
    print(f"El promedio de temperatura en la ciudad de {ciudad} es {promedios[i]:.2f}°C")
