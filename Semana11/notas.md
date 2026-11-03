1. Introducción al Consumo de APIs
El consumo de APIs se refiere al proceso mediante el cual una aplicación cliente (como una página web, una app móvil o un servidor backend) realiza solicitudes (requests) a un servidor externo o interno a través de un protocolo estándar (generalmente HTTP/HTTPS) para obtener, enviar, actualizar o eliminar datos.

2. Conceptos Clave y Terminología
Cliente: La aplicación o sistema que realiza la petición (ej. React, Postman, una app en Python).

Servidor (API Provider): El sistema que recibe la petición, procesa la lógica de negocio y devuelve una respuesta.

Endpoint: La URL específica donde se puede acceder a un recurso de la API (ej. [https://api.ejemplo.com/v1/usuarios](https://api.ejemplo.com/v1/usuarios)).

Métodos HTTP (Verbos): Indican la acción que se desea realizar sobre el recurso:

GET: Obtener recursos o datos.

POST: Crear un nuevo recurso.

PUT: Actualizar un recurso existente (reemplazo completo).

PATCH: Modificar parcialmente un recurso.

DELETE: Eliminar un recurso.

3. Arquitectura y Formatos de Datos
Los formatos más comunes para el intercambio de datos en las APIs modernas son:

JSON (JavaScript Object Notation): El estándar de la industria por su ligereza y facilidad de lectura tanto para humanos como para máquinas.

XML: Usado principalmente en sistemas empresariales heredados o protocolos SOAP.

Ejemplo de una respuesta típica en formato JSON:

JSON
{
  "status": "success",
  "data": {
    "id": 102,
    "nombre": "Ana Gómez",
    "correo": "ana.gomez@example.com"
  }
}
4. Métodos de Autenticación y Seguridad
Para consumir APIs de forma segura, los proveedores implementan mecanismos de autenticación:

API Keys: Una clave secreta enviada generalmente en los encabezados (headers) de la petición o parámetros de la URL. Ideal para identificaciones simples.

Bearer Tokens (JWT - JSON Web Tokens): Tokens de acceso temporal firmados criptográficamente que se envían en el encabezado Authorization: Bearer <token>.

OAuth 2.0: Protocolo estándar de autorización para permitir que aplicaciones terceras accedan a recursos sin exponer las credenciales del usuario.

Basic Auth: Envío de usuario y contraseña codificados en Base64 (requiere uso estricto de HTTPS).

5. Códigos de Estado HTTP
Al consumir una API, el servidor siempre responde con un código numérico que indica el resultado de la operación:

Rango	Categoría	Significado Común
2xx	Éxito	La petición fue recibida, entendida y procesada correctamente (200 OK, 201 Created).
4xx	Error del Cliente	La petición contiene errores o faltan credenciales (400 Bad Request, 401 Unauthorized, 404 Not Found).
5xx	Error del Servidor	Ocurrió un fallo en el servidor al procesar la solicitud (500 Internal Server Error, 503 Service Unavailable).
6. Ejemplo Práctico de Consumo (JavaScript / Fetch API)
A continuación, se muestra cómo realizar una petición GET y una petición POST utilizando JavaScript moderno:

Petición GET (Obtener datos)
import requests

def obtener_info_pokemon(nombre_pokemon):
    # Endpoint de la PokéAPI para un Pokémon en específico (convertido a minúsculas)
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}"
    
    try:
        # Realizamos la petición GET
        respuesta = requests.get(url)
        
        # Verificamos si la petición fue exitosa (código 200)
        if respuesta.status_code == 200:
            # Convertimos la respuesta a un diccionario de Python (JSON)
            datos = respuesta.json()
            
            nombre = datos['name'].capitalize()
            id_pokemon = datos['id']
            altura = datos['height'] / 10  # En la API viene en decímetros, lo pasamos a metros
            peso = datos['weight'] / 10    # En la API viene en hectogramos, lo pasamos a kilogramos
            
            # Extraemos los tipos del Pokémon
            tipos = [tipo['type']['name'] for tipo in datos['types']]
            
            print(f"¡Pokémon encontrado!")
            print(f"ID: #{id_pokemon}")
            print(f"Nombre: {nombre}")
            print(f"Altura: {altura} m")
            print(f"Peso: {peso} kg")
            print(f"Tipo(s): {', '.join(tipos)}")
            
        elif respuesta.status_code == 404:
            print(f"Error: No se encontró al Pokémon '{nombre_pokemon}'. Revisa el nombre.")
        else:
            print(f"Error inesperado: Código de estado {respuesta.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error de conexión: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    obtener_info_pokemon("pikachu")

