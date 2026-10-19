nombres = [
    "Raul", "Sergio", "Karla", "Alejandro", "Lucía", 
    "Carlos", "María", "Javier", "Elena", "Daniel", 
    "Sofía", "David", "Paula", "Adrián", "Carmen", 
    "Manuel", "Laura", "Pablo", "Beatriz", "Fernando", 
    "Sara", "Diego", "Claudia", "Mateo", "Valeria", 
    "Ángel", "Natalia", "Héctor", "Patricia", "Gabriel", 
    "Andrea", "Mario", "Silvia", "Roberto", "Monica", 
    "Ricardo", "Lorena", "Francisco", "Irene", "Alberto", 
    "Victoria", "Rubén", "Adriana", "Jorge", "Marina", 
    "Guillermo", "Teresa", "Alvaro", "Rocío", "Ignacio"
]

# usando in en un ciclo determinamos 2 cosas 1) la capacidad y 2) la cantidad de elementos

for nombre in nombres:
    print(f"Hola {nombre} como estas")

# Usando range
# range simple inica en 0 y termina un numero antes del definido

for numero in range(5):
    print(numero-1)


# range con inicio fin e interacion
for nnum in range(10, 20, 2):
    print(nnum)

