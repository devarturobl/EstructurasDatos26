import requests

# URL de la API de ejemplo
url = "https://randomuser.me/api/"

# Realizar la petición GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    print("¡Solicitud exitosa!")
    # Convertir la respuesta a formato JSON (diccionario de Python)
    data = response.json()
    print("Nombre:", data["results"][0]["name"]["title"], data["results"][0]["name"]["first"], data["results"][0]["name"]["last"])
    print("Email:", data["results"][0]["email"])
    print("Ciudad:", data["results"][0]["location"]["city"])
else:
    print("Error en la solicitud:", response.status_code)
