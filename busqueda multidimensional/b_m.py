valor_buscado = input("Ingrese un numero a buscar: ")

bidimensional = [[30, 93], [49, 17], [3, 84], [77, 13],
                 [59, 62], [12, 35], [29, 12], [80, 55],
                 [94, 15], [7, 1], [92, 96], [41, 60]]
print("Matriz:", bidimensional)
encontrado = False
for fila in range(len(bidimensional)):
    for columna in range(len(bidimensional[0])):
        numero_buscado = bidimensional[fila][columna]
        if numero_buscado == valor_buscado:
            encontrado = True
            posicion = (fila, columna)
            break

if encontrado:
    print(f"\nEl indice del numero {valor_buscado} es: ({posicion})")
else:
    print(f"\nEl numero {valor_buscado} no se encuentra")
