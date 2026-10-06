datos = [5, 8, 2, 1]

# Método de la burbuja
for x in range(len(datos) - 1):
    print("Valor de x:", x)
    for y in range(len(datos) - 1 - x):
        print("Valor de y:", y)
        if datos[y] > datos[y + 1]:
            # Intercambio (swap)
            burbuja = datos[y]
            datos[y] = datos[y + 1]
            datos[y + 1] = burbuja
            print("Valor de burbuja:", burbuja)

print("Datos ordenados:", datos)
