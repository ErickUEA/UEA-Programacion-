matriz = [[44, 688, 984], [950, 501, 770],
          [145, 315, 681], [567, 990, 906],
          [691, 752, 10], [802, 586, 180],
          [230, 12, 996], [558, 889, 359]
          ]

print(f"La siguiente matriz esta desordenada")
print(matriz)
fila_a_ordenar = int(input("cual fila desea ordenar: "))
for i in range(len(matriz[fila_a_ordenar]) - 1):
    for j in range(len(matriz[fila_a_ordenar]) - i - 1):
        if matriz[fila_a_ordenar][j] > matriz[fila_a_ordenar][j + 1]:
            matriz[fila_a_ordenar][j], matriz[fila_a_ordenar][j + 1] = matriz[fila_a_ordenar][j + 1], matriz[fila_a_ordenar][j]

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la fila {} ordenada:".format(fila_a_ordenar))
for fila in matriz:
    print(fila)
