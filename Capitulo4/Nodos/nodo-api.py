# coding=utf-8

# pip3 install requests 

import requests
import json

# Configuración de conexión con Thingsboard
url = "http://10.0.2.83/api/v1/A1_TEST_TOKEN/telemetry"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Authorization": "Bearer A1_TEST_TOKEN"
}

# Crear un diccionario con los valores de los parámetros
data = {
    "temperature": 25.0,
    "humidity": 60.0
}

# Convertir el diccionario a un formato JSON
payload = json.dumps(data)

# Enviar la solicitud HTTP POST
response = requests.post(url, headers=headers, data=payload)

# Verificar el estado de la respuesta
if response.status_code == 200:
    print("Mensaje enviado con éxito a Thingsboard")
else:
    print("Error al enviar el mensaje a Thingsboard")

