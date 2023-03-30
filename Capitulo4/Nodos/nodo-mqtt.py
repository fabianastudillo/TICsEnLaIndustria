# coding=utf-8

import paho.mqtt.publish as publish
import json

# Configuración de conexión con Thingsboard
THINGSBOARD_HOST = 'localhost'
ACCESS_TOKEN = 'dDGBB2QacLxCh2knhO5Q'

# Crear un diccionario con los valores de los parámetros
data = {
    "timestamp": 3504160841,
    "value": 3.630000114
}

# Convertir el diccionario a un formato JSON
payload = json.dumps(data)

# Publicar el mensaje en el topic específico del dispositivo
topic = 'v1/devices/me/telemetry'
publish.single(topic, payload=payload, hostname=THINGSBOARD_HOST, port=1883, auth={'username':ACCESS_TOKEN})

# Verificar que se envió el mensaje correctamente
print("Mensaje enviado con éxito a Thingsboard")

