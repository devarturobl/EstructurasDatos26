# Variables Ejemplo 1 entro y decimal
entero = 10
decimal = 3.14

print("El valor de la variable entero es:", entero)
print("El valor de la variable decimal es:", decimal)   
print(f"El valor de la variable entero es: {entero} y el valor de la variable decimal es: {decimal} suman {entero + decimal}")

# Variables Ejemplo 2 cadena de texto
cadena = "Hola, soy Jazmin y estudio sistemas computacionales"
print("El valor de la variable cadena es:", cadena)


# Ejemplo de un arreglo de enteros
aentero = [7, 9, 3, 1, 5]
print("El valor de la variable aentero es:", aentero)
print(f"El valor 1 de la variable aentero es: {aentero[0]}")
print(f"El valor 2 de la variable aentero es: {aentero[1]}")
print(f"El valor 3 de la variable aentero es: {aentero[2]}")
print(f"El valor 4 de la variable aentero es: {aentero[3]}")
print(f"El valor 5 de la variable aentero es: {aentero[4]}")

# Ejemplo de una lista y metodos
lista = []
print("Valores de la lista:", lista)

# Agregar elementos a la lista
lista.append(10)
lista.append(6)
lista.append(2)
print("Valores de la lista:", lista)

# Lista metodo extend() agrega multiples elementos a la lista
lista.extend([1, 2, 3, 9, 10, 11, 80])
print("Valores de la lista:", lista)

# Lista ejemplo sort
lista.sort()
print("Valores de la lista ordenados:", lista)

# Lista con diferentes tipos de datos
directorio = [20, "Hola", 3.14, True]
print("Valores del directorio:", directorio)

# Ejemplo de una estructura de datos
miestructura = {
    "nombre": "Jazmin",
    "direccion": "Calle 123",
    "telefono": "555-1234"
}

print("Estructura de datos:", miestructura)
print("Nombre:", miestructura["nombre"])
print("Direccion:", miestructura["direccion"])
print("Telefono:", miestructura["telefono"])

miarrayestructura = [
    {
        "nombre": "Jazmin",
        "direccion": "Calle 123",
        "telefono": "555-1234"
    },
    {
        "nombre": "Juan",
        "direccion": "Calle 456",
        "telefono": "555-5678"
    },
    {
        "nombre": "Maria",
        "direccion": "Calle 789",
        "telefono": "555-9012"
    },
    {
        "nombre": "Pedro",
        "direccion": "Calle 321",
        "telefono": "555-3456"
    }
]

print("Mostrar todos los datos de mi arreglo de estructuras:", miarrayestructura)
print("Mostrar el nombre de la primera persona:", miarrayestructura[0]["nombre"], miarrayestructura[0]["telefono"])