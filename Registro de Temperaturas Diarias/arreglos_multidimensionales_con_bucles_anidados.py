# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Semanas (3 semanas)
# Tercera dimensión: Días de la semana (7 días)
# datos obtenidos de: https://shre.ink/rTgW
ciudades = ["Ambato", "Tena"]
temperaturas = [
    [  # {cuidad_1}
        [  # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [  # Tena
        [  # Semana 1
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 28}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
promedios = []
for ciudad, datos in zip(ciudades, temperaturas):
    promedios_ciudad = []
    for semana in datos:
        suma_temp = 0
        for dia in semana:
            suma_temp += dia["temp"]
        promedio_semana = suma_temp / len(semana)
        promedios_ciudad.append(promedio_semana)
    promedios.append(promedios_ciudad)

for i, ciudad in enumerate(ciudades):
    print(f"Cuidad: {ciudad}")
    for j, promedio in enumerate(promedios[i]):
        print(f"  Semana {j + 1}: {promedio:.2f}")
