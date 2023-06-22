''' 

======== Connexion au serveurs : =========

Base de données :

'''

UsrBDD = 'adminsae24'   # Nom utilisateur pour la Base de Données
pswBDD = 'passroot'   # Mot de passe de l'utilisateur
AddrBDD = '192.168.195.134'   # Adresse de la Base de Données
nomBDD = 'sae24'   # Nom de la Base de Données


'''
Broker MQTT :

'''
AddrMqtt = '192.168.195.236'   # Adresse du broker MQTT
prtMqtt = 1883   # Port du Broker MQTT
tpcMqtt = 'topic_micro'   # Topic sur lequel s'abonner
'''

========================================================================================================================================================================

'''

import paho.mqtt.client as mqtt


import mysql.connector as mysql
from mysql.connector import Error


cooObj = None

def connexion_test_mqtt():

    def on_connect(client, userdata, flags, rc):

        client.subscribe(tpcMqtt)

    BrokerSaE24 = mqtt.Client()

    def on_message(client, userdata, message):

        print("test :", message)
        print("message reçu: "  + str(message.payload.decode("utf-8")))
        print("message topic: "+ message.topic)


    BrokerSaE24 = mqtt.Client()

    BrokerSaE24.on_connect = on_connect
    BrokerSaE24.on_message = on_message


    BrokerSaE24.connect(AddrMqtt, 1883, 60)


    BrokerSaE24.loop_forever()



def connexion_test_sql():



    def TestBDDReception():

        search_query = "SELECT Num_case FROM Ampli-mic"
        cursor.execute(search_query)

        cooObj = cursor.fetchall()
        print(cooObj[-1])

        return cooObj


    def TestBDDEnvoi():

        BDDSaE24.commit()

        insert_query = "INSERT INTO table1 (ID, NumeroCase) VALUES (%s, %s)"
        cursor.execute(insert_query, (8, 18))

        BDDSaE24.commit()


    print(pswBDD)

    BDDSaE24 = mysql.connect(user=UsrBDD, password=pswBDD,host=AddrBDD,database=nomBDD)

    cursor = BDDSaE24.cursor()


    #TestBDDEnvoi()
    TestBDDReception()


    cursor.close()
    BDDSaE24.close()

'''
try :

    connexion_test_sql()
except Error as erreur :
    print("\n marche pas :\n\n", erreur)
'''


connexion_test_mqtt()

