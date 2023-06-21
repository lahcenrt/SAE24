''' ALGO

declaration :


mAmp <- tableau contenant : (Ampm1, Ampm2, Ampm3 )
cooObj <- tableau de 2 float : (x,y)


query : 


cooObj <- SELECT coordonné FROM Nabil where Ampmicro1 = Ampm1 and Ampmicro2 = Ampm3 and Ampmicro3 = Ampm3

INSERT INTO Abdel(coordonée) VALAUES(:cooObj)



'''

from mysql.connector import *
import paho.mqtt.client as mqtt
from json import *

# ==================== Déclaration des Variables ==================== #

cooObj = None

mAmp = {}

# ==================== Déclaration des Fonctions ==================== #

def JSON(msg, obj):
    
    msg = msg.payload.decode()
    msg = msg[obj]
    
    return msg 

def on_message(client, userdata, message):

    mAmp["Ampm1"] = JSON(message, "Ampmicro1")
    mAmp["Ampm2"] = JSON(message, "Ampmicro2")
    mAmp["Ampm3"] = JSON(message, "Ampmicro3")

def correspondance_coo_amp(Amp):

    cursor.execute("SELECT Num_case FROM Ampli-mic WHERE Mic1BG = %s AND Mic2HG = %s AND Mic3HD = %s", (mAmp["Ampm1"], mAmp["Ampm2"], mAmp["Ampm3"]))

    cooObj = cursor.fetchfirst()

    return cooObj

def envoi_coo(cooObj):

    cursor.execute("INSERT INTO For-ws(Num_case, Mic1BG, Mic2HG, Mic3HD) VALUES(%s, %s, %s, %s) ",(cooObj, mAmp["Ampm1"], mAmp["Ampm2"], mAmp["Ampm3"]))


# ==================== Connection au serveurs ==================== #

# Base de Données #
BDDSaE24 = mysql.connector.connect(user='admin', password='passroot',host='127.0.0.1',database='sae24(2).sql')

cursor = BDDSaE24.cursor()

# Broker MQTT #
BrokerSaE24 = mqtt.Client()
BrokerSaE24.connect("ADDRESSE MQTT")
BrokerSaE24.subscribe("NOM du topic")
BrokerSaE24.loop_start()


# ==================== Querys ==================== #

BrokerSaE24.on_message = envoi_coo(correspondance_coo_amp(on_message))


cursor.close()
BDDSaE24.close()