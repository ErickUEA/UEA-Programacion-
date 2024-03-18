# Se crea un diccionario de nombre informacion_personal
informacion_personal = {"nombre": "Patricia", "edad": 18, "cuidad": "Puyo"}
# Imprime el diccionario original
print("Diccionario original", informacion_personal)
# Se cambia el valor de la clave "cuidad" por Ambato
informacion_personal["cuidad"] = "Ambato"
# Se imprime el diccionario con la ciudad cambiada
print("\nCuidad Modificada: ", informacion_personal)
# Se añade la clave profesion con un valor cualquiera
informacion_personal["profesion"] = "Estudiante"
# Se imprime la adición de la profesion
print("\nProfresion añadida: ", informacion_personal)
# Se verifica si el teléfono existe en el diccionario
if "Teléfono" in informacion_personal:
    print(informacion_personal)
else:
    # mensaje de que no existe el número de teléfono
    print("\nNo existe numero de teléfono, añadiendo uno =)")
    # Se añade la clave "Teléfono" con un valor cualquiera
    informacion_personal["Teléfono"] = "0991278250"
    # Se imprime el teléfono
    print(informacion_personal)
# Se borra la edad del diccionario
del informacion_personal["edad"]
# Se imprime el diccionario final con la edad eliminada
print("\nEdad eliminada y Diccionario resultante: ", informacion_personal)

