''' 

========================================================================================================================================================================

Programme permettant la correspondance entre :

les amplitudes enregistrer par 3 microphones. (reçu à travers un Broker MQTT)

    et

la position de l'objet ayant émis le bruit capté par les 3 microphones. (pour l'envoyer dans une base de données SQL)

======== Connexion au serveurs : =========

Base de données :

'''

UsrBDD = ''   # Nom utilisateur pour la Base de Données
pswBDD = ''   # Mot de passe de l'utilisateur
AddrBDD = ''   # Adresse de la Base de Données
nomBDD = ''   # Nom de la Base de Données


'''
Broker MQTT :

'''
AddrMqtt = ""   # Adresse du broker MQTT
prtMqtt = ""   # Port du Broker MQTT
tpcMqtt = ""   # Topic sur lequel s'abonner
'''

========================================================================================================================================================================

'''


import mysql.connector as mysql
from mysql.connector import Error

import paho.mqtt.client as mqtt

from json import *

# ==================== Déclaration des Variables ==================== #

envoiFINI = False

# ==================== Déclaration des Fonctions ==================== #

def JSON(msg, obj):
    
    msg = msg.payload.decode()
    msg = msg[obj]
    
    return msg 

## Envoi de la position actuelle de l'objet dans la BDD ##

def envoi_coo(cooObj,Amp):

    cursor.execute("INSERT INTO For-ws(Num_case, cdMic1BG, cdMic2HG, cdMic3HD) VALUES(%s, %s, %s, %s) ",(cooObj, Amp["Ampm1"], Amp["Ampm2"], Amp["Ampm3"]))
    envoiFINI = True

## Correspondance amplitudes / position de l'objet , à l'aide de la BDD ##

def correspondance_coo_amp(Amp):

    cooObj = None

    cursor.execute("SELECT Num_case FROM Ampli-mic WHERE Mic1BG = %s AND Mic2HG = %s AND Mic3HD = %s", (Amp["Ampm1"], Amp["Ampm2"], Amp["Ampm3"]))

    cooObj = cursor.fetchfirst()

    return cooObj

## A la reception d'un message MQTT ##

def on_message(client, userdata, message):

    mAmp = {}

    print("message reçu: "  + str(message.payload.decode("utf-8")))
    print("topic du message : "+ message.topic)

    if message.topic == "topic_micro/mic1" :
        mAmp["Ampm1"] = JSON(message, "mic1")
        print("Ajouter à Micro1: "+ message.payload.decode())
    elif message.topic == "topic_micro/mic2" :
        mAmp["Ampm1"] = JSON(message, "mic2")
        print("Ajouter à Micro2: "+ message.payload.decode())
    elif message.topic == "topic_micro/mic3" :
        mAmp["Ampm1"] = JSON(message, "mic3")
        print("Ajouter à Micro3: "+ message.payload.decode())

    if mAmp["Ampm1"] == True and mAmp["Ampm2"] == True and mAmp["Ampm3"] == True :      #Si les 3 Amplitutes sont reçu :

        envoi_coo(correspondance_coo_amp(mAmp), mAmp)                                   #Envoyé les données

    if envoiFINI == True :
        print('Envoi effectué')
        envoiFINI = False
    

# ==================== Connection au serveurs ==================== #

# Broker MQTT #

def on_connect(client, userdata, flags, rc):

    client.subscribe(tpcMqtt)

def connexionMQTT():

    BrokerSaE24 = mqtt.Client()

    BrokerSaE24.on_connect = on_connect
    BrokerSaE24.on_message = on_message

    BrokerSaE24.connect(AddrMqtt, prtMqtt, 60)

    BrokerSaE24.loop_forever()

# Base de Données #

def connexionBDD():

    BDDSaE24 = mysql.connector.connect(user=UsrBDD, password=pswBDD,host=AddrBDD,database=nomBDD)

    cursor = BDDSaE24.cursor()

    return cursor

# ==================== Execution ==================== #

try:
    cursor = connexionBDD()
except Error as erreur:
    print("\n # Connexion à la Base de données impossible, vérifier les informations de connexion en tête de fichier #\n\n", erreur)

connexionMQTT()

cursor.close()