#Repaso sobre estructuras y tipos de datos en Python

# Ejemplo de una estructura de datos y directorios
misalumnos = [
    {
        "nombre": "Ismerai",
        "apaterno": "Velazco",
        "amaterno": "Castillo",
        "edad": 18,
    },
    {
        "nombre": "Yaretzi",
        "apaterno": "Hernandez",
        "amaterno": "Patricio",
        "edad": 19,
    },
    {
        "nombre": "Jesus Manuel",
        "apaterno": "Sanchez",
        "amaterno": "Pereyra",
        "edad": 18,
    },
    {
        "nombre": "Francisco",
        "apaterno": "Juarez",
        "amaterno": "Avendaño",
        "edad": 19,
    },
    {
        "nombre": "Jeremy",
        "apaterno": "Hernandez",
        "amaterno": "Robles",
        "edad": 19,
    },
    {
        "nombre": "Giovanni",
        "apaterno": "Cuello",
        "amaterno": "Jinez",
        "edad": 20,
    },
]

print("Mostrar todos los datos de mis alumnos:", misalumnos)
print("Mostrar solo el registro del primer alumno:", misalumnos[0])

#Buscar un alumno por nombre
nalumno = "Giovanni"

for alumno in misalumnos:
    if alumno["nombre"] == nalumno:
        print("Alumno encontrado:", alumno)
        break




