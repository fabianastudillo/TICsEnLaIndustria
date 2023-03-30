import pandas as pd
import time
import paho.mqtt.client as mqtt
from datetime import datetime

Delta=8
# Configuración del broker MQTT y del dispositivo en ThingsBoard
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
ACCESS_TOKEN = "dDGBB2QacLxCh2knhO5Q"
# DEVICE_ID = "124e0f30-ceed-11ed-9137-112aa0370fe7"

# Leer el archivo CSV
df = pd.read_csv("./grindingData.txt", header=None, names=["timestamp","SETPOINT_ADITIVO"],dtype={"timestamp": int, "SETPOINT_ADITIVO": float}, usecols=["timestamp", "SETPOINT_ADITIVO"], sep="\t")

# Calcular el tiempo entre registros
timestamps = df["timestamp"]
time_diffs = [0] + [(timestamps[i] - timestamps[i-1])/1000 for i in range(1, len(timestamps))]

# Configuración del cliente MQTT
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(MQTT_BROKER, MQTT_PORT)

current_timestamp = int(time.time())*1000
timestamp=current_timestamp
# Enviar los valores del campo SETPOINT_ADITIVO a ThingsBoard en función del tiempo entre registros
for i, row in df.iterrows():
    setpoint_aditivo = row["SETPOINT_ADITIVO"]
    time_diff = time_diffs[i]
    time.sleep(time_diff*Delta)
    #time.sleep(1000)
    #print("La hora es:", time.strftime("%H:%M:%S"))
    #print(time_diff)
#    message = '{{"ts": {timestamp}, "values": {{"SETPOINT_ADITIVO": {setpoint_aditivo}}}}}'.format(
#        timestamp=int(row["timestamp"]),
#        setpoint_aditivo=setpoint_aditivo
#    )
    message = '{{"ts": {timestamp}, "values": {{"SETPOINT_ADITIVO": {setpoint_aditivo}}}}}'.format(
        timestamp=timestamp,
        setpoint_aditivo=setpoint_aditivo
    )
#    print(message)
    client.publish("v1/devices/me/telemetry", message)
    #timestamp+=1000
    timestamp+=(time_diff*1000)*Delta
    

# Cerrar la conexión con el broker MQTT
client.disconnect()

