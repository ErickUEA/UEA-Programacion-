# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
# datos obtenidos de: https://shre.ink/rTgW
ciudades = ["Ambato", "Tena"]
temperaturas = [
    [
        [
            "Lunes", 24,
            "Martes", 26,
            "Miércoles", 25,
            "Jueves", 23,
            "Viernes", 24,
            "Sábado", 25,
            "Domingo", 26
        ],
        [
            "Lunes", 26,
            "Martes", 27,
            "Miércoles", 27,
            "Jueves", 31,
            "Viernes", 28,
            "Sábado", 16,
            "Domingo", 16
        ],
        [
            "Lunes", 29,
            "Martes", 31,
            "Miércoles", 29,
            "Jueves", 29,
            "Viernes", 31,
            "Sábado", 29,
            "Domingo", 26
        ]
    ],
    [
        [
            "Lunes", 29,
            "Martes",  31,
            "Miércoles", 29,
            "Jueves", 28,
            "Viernes", 27,
            "Sábado", 30,
            "Domingo", 31
        ],
        [
            "Lunes", 30,
            "Martes", 32,
            "Miércoles", 31,
            "Jueves", 30,
            "Viernes", 29,
            "Sábado", 29,
            "Domingo", 30
        ],
        [
            "Lunes", 31,
            "Martes",  29,
            "Miércoles", 30,
            "Jueves", 29,
            "Viernes", 30,
            "Sábado", 32,
            "Domingo", 28
        ]
    ]
]
# Recorrer la lista de temperaturas y calcular el promedio para cada ciudad y semana
for ciudad, ciudad_temperaturas in enumerate(temperaturas):
    for semana_index, semana_temperaturas in enumerate(ciudad_temperaturas):
        dias = semana_temperaturas[::2]  # Obtener los días
        temps = semana_temperaturas[1::2]  # Obtener las temperaturas
        promedio_temp = sum(temps) / len(temps)  # Calcular el promedio
        print(f"Promedio de temperaturas para la ciudad {ciudades[ciudad]} y la semana {semana_index + 1}:")
        for dia, temp in zip(dias, temps):
            print(f"{dia}: {temp}°C")