def convertir(grados_centi):
    Fahrenheint = (9 / 5) * (grados_centi) + 32
    Kelvin = 273.15 + grados_centi

    return Fahrenheint, Kelvin


centigrado = int(input("Ingrese grados centigrados: "))

far, kel = convertir(centigrado)

print(f"{centigrado}°C es igual a {far}°F")
print(f"{centigrado}°C es igual a {kel}°K")
