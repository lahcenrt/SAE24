

def JSON(msg, obj):
    
    msg = msg.payload.decode()
    msg = msg[obj]
    
    return msg 

def connexion_test_mqtt():

    import paho.mqtt.client as mqtt


    def on_connect(client, userdata, flags, rc):

        client.subscribe("Student/by-room")

    BrokerSaE24 = mqtt.Client()

    def on_message(client, userdata, message):

        message_content = str(message.payload.decode("utf-8")) 
        print("message reçu: "  + str(message.payload.decode("utf-8")))
        print("message topic: "+ message.topic)


    BrokerSaE24 = mqtt.Client()

    BrokerSaE24.on_connect = on_connect
    BrokerSaE24.on_message = on_message


    BrokerSaE24.connect("mqtt://mqtt.iut-blagnac.fr", 1883, 60)


    BrokerSaE24.loop_forever()




def connexion_test_sql():

    import mysql.connector as mysql

    def correspondance_coo_amp(Amp):

        cursor.execute("SELECT Num_case FROM Ampli-mic WHERE Mic1BG = %s AND Mic2HG = %s AND Mic3HD = %s", (mAmp["Ampm1"], mAmp["Ampm2"], mAmp["Ampm3"]))

        cooObj = cursor.fetchone()

        return cooObj



    mAmp = {}

    mAmp["Ampm1"] = '0.0449'
    mAmp["Ampm2"] = '0.0243'
    mAmp["Ampm3"] = '0.0268'





    BDDSaE24 = mysql.connect(user='4208885_testbdd', password='testBDD123',host='fdb1027.eohost.com',database='4208885_testbdd')

    cursor = BDDSaE24.cursor()




    correspondance_coo_amp(mAmp)




    cursor.close()
    BDDSaE24.close()

connexion_test_sql()