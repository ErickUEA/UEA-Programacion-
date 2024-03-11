#   Definir la funcion calcular_descuento
def calcular_descuento(monto_t, porcentaje_des=20):
    descuento = monto_t * (porcentaje_des / 100)
    return descuento


# Primera llamada
compra_1 = int(input("Ingrese el valor de la compra 1: "))
des_1 = calcular_descuento(compra_1)
monto_final_1 = compra_1 - des_1
# Aqui se imprime de manera bonita el resultado
print("\n┌-------------------------------------------------------------------┐")
print(f"| Monto de compra 1: {compra_1}$                                          |")
print(f"| Descuento aplicado a la compra 1: {des_1:.2f}$                        |")
print(f"| Valor total al pagar de la compra 1: {monto_final_1:.2f}$                     |")
print("└-------------------------------------------------------------------┘")
# Segunda llamada
compra_2 = int(input("\n Ingrese el valor de la compra 2: "))
porcentaje_des = int(input("Ingrese el porcentaje del descuento: "))
des_2 = calcular_descuento(compra_2, porcentaje_des)
monto_final_2 = compra_2 - des_2
print("\n┌-------------------------------------------------------------------┐")
print(f"| Monto de compra 2: {compra_2}$                                          |")
print(f"| Porcentaje de descuento a la compra 2: {porcentaje_des}%                        |")
print(f"| Descuento aplicado a la compra 2: {des_2:.2f}$                        |")
print(f"| Valor total al pagar de la compra 2: {monto_final_2:.2f}                      |")
print("└-------------------------------------------------------------------┘")
