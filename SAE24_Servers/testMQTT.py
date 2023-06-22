import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connexion réussie")
    else:
        print(f"Problème de connexion, code = {rc}")

def on_message(client, userdata, message):
    print(f"message reçu: {str(message.payload.decode('utf-8'))}")

client = mqtt.Client("P1") 

client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("192.168.195.236") 
    client.loop_start() 
    client.subscribe("topic_micro")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
finally:
    client.loop_stop()