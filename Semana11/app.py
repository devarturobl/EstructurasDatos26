import requests

# Define the URL of the API endpoint
url = "https://pokeapi.co/api/v2/pokemon/"

# Consumo de api por el metodo get
midata = requests.get(url)

print(f"Los datos del api sin formato solo respuesta: {midata}")

# Cambiar el formato de la respuesta a json
midata_json = midata.json()

print(f"Los datos del api en formato json: {midata_json}")

# Obtener solo el conteo
print(f"El conteo de pokemones es: {midata_json['count']}")
# Otro ejemplo pero con el valor de next
print(f"La url de la siguiente pagina es: {midata_json['next']}")
# Ejemplo mostrando el contenido de results que es un arreglo de objetos
print(f"El contenido de results es: {midata_json['results']}")

# Ejemplo mostrando el nombre del primer pokemon y el nombre del pokemon en la posicion 19
print(f"El nombre del primer pokemon es: {midata_json['results'][0]}")
print(f"El nombre del pokemon posicion 19 es: {midata_json['results'][19]}")

# Ejemplo mostrando el nombre del primer pokemon
print(f"El nombre del primer pokemon es: {midata_json['results'][0]['name']}")

for pokemon in midata_json['results']:
    print(f"El nombre del pokemon es: {pokemon['name']}")

