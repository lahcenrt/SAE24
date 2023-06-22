''' 

========================================================================================================================================================================

Programme permettant la correspondance entre :

les amplitudes enregistrer par 3 microphones. (reçu à travers un Broker MQTT)

    et

la position de l'objet ayant émis le bruit capté par les 3 microphones. (pour l'envoyer dans une base de données SQL)

======== Connexion au serveurs : =========

Database :

'''

UsrBDD = 'adminsae24'   # Username
pswBDD = 'passroot'   # Password
AddrBDD = '127.0.0.1'   # Host address
nomBDD = 'sae24'   # Database name


'''
Broker MQTT :

'''
AddrMqtt = "192.168.159.33"   # Host address
prtMqtt = 1883   # Port 
tpcMqtt = 'topic_micro/#'   # Topic 
'''

========================================================================================================================================================================

'''


import mysql.connector as mysql
from mysql.connector import Error

import paho.mqtt.client as mqtt

import json
import subprocess


# ==================== Variables Declaration ==================== #

envoiFINI = False

# ==================== Fonctions Declaration ==================== #

## convertion from JSON to python variable ##

def convJSON(msg, obj):

    msg = str(msg.payload.decode("utf-8"))
    msgDICO = json.loads(msg)
    
    return msgDICO[obj]

## Sending the object current location to the database ##

def envoi_coo(cooObj):

    print('Envoi en cours : ',cooObj)

    # Calling the shell script QueryEnvoi.sh
    subprocess.call(['./QueryEnvoi.sh', str(cooObj)])

    envoiFINI = True

## Using the database to match the microphones datas with the object location ##

def correspondance_coo_amp(Amp):

    cooObj = None

    QueryComp = "SELECT Num_case FROM Ampli_mic WHERE cdMic1BG = '{}' AND cdMic2HG = '{}' AND cdMic3HD = '{}'".format(Amp["Ampm1"], Amp["Ampm2"], Amp["Ampm3"])

    cursor.execute(QueryComp)

    cooObj = cursor.fetchone()

    print('Position actuelle de l objet :', cooObj[0] )

    return cooObj[0]

## When recieving a MQTT message : ##

def on_message(client, userdata, message):
    print('\nreçu!')
    mAmp = {}

    print("topic du message : "+ message.topic)

    if message.topic == "topic_micro/microphones" :
        mAmp["Ampm1"] = convJSON(message, "mic1")
        mAmp["Ampm2"] = convJSON(message, "mic2")
        mAmp["Ampm3"] = convJSON(message, "mic3")

        print("\nAjouter à Micro 1: ", mAmp["Ampm1"])
        print("Ajouter à Micro 2: ", mAmp["Ampm2"])
        print("Ajouter à Micro 3: ", mAmp["Ampm3"])

    if mAmp["Ampm1"] == True and mAmp["Ampm2"] == True and mAmp["Ampm3"] == True :      # If all 3 amplitutes are received :

        print('\n Triangulation :\n')
        envoi_coo(correspondance_coo_amp(mAmp))                                   # Sending data
     




## MQTT Simulation ##

def test(message):
    print('\nreçu!')
    mAmp = {}

    print("message reçu: ",message)
    print("topic du message : oui")

    if message:
        mAmp["Ampm1"] = message["mic1"] 
        mAmp["Ampm2"] = message["mic2"] 
        mAmp["Ampm3"] = message["mic3"] 

        print("\nAjouter à Micro 1: ", mAmp["Ampm1"])
        print("Ajouter à Micro 2: ", mAmp["Ampm2"])
        print("Ajouter à Micro 3: ", mAmp["Ampm3"])

    if mAmp["Ampm1"] and mAmp["Ampm2"] and mAmp["Ampm3"]:                         # If all 3 amplitutes are received :

        print('\n c est partis mon kiki\n')
        envoi_coo(correspondance_coo_amp(mAmp))                                   # Sending data




# ==================== Connection to the servers ==================== #

# Broker MQTT #

def on_connect(client, userdata, flags, rc):

    client.subscribe(tpcMqtt)
    print("\nMQTT Server connecté ")


def connexionMQTT():

    BrokerSaE24 = mqtt.Client()

    BrokerSaE24.on_connect = on_connect
    BrokerSaE24.on_message = on_message

    BrokerSaE24.connect(AddrMqtt, prtMqtt, 60)

    BrokerSaE24.loop_forever()

# Base de Données #       

def connexionBDD():

    BDDSaE24 = mysql.connect(user=UsrBDD, password=pswBDD,host=AddrBDD,database=nomBDD)

    return BDDSaE24

# ==================== Execution ==================== #

try:
    BDDSaE24 = connexionBDD()
    cursor = BDDSaE24.cursor()

    if BDDSaE24.is_connected():
            
            db_Info = BDDSaE24.get_server_info()
            print("MySQL Server connecté : ", db_Info)
            
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Connecté a la base: ", record)

            connexionMQTT()
            #test({"mic1": "100110","mic2": "101101","mic3": "111","last_position": 130})

except Error as e:
        print("\n # Erreur sur la Base de données, vérifier les informations de connexion en tête de fichier #\n\n", e)

finally:
        if (BDDSaE24.is_connected()):
            cursor.close()
            BDDSaE24.close()
            print("\n # MySQL Server Déconnecté #\n")


#TODO QueryEnvoi(fonctionne) + affiché de M1 a M3