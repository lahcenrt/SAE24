import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',  # L'adresse de l'hôte, généralement localhost ou l'adresse IP du serveur
                                         database='sae24',  # Le nom de la base de données à laquelle vous souhaitez vous connecter
                                         user='adminsae24',  # Le nom d'utilisateur que vous utilisez pour vous connecter à MySQL
                                         password='passroot')  # Le mot de passe associé à votre nom d'utilisateur

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        QueryTest = "SELECT `{}` FROM `{}`;".format('login','Admin')
        cursor.execute(QueryTest)

        TestData = cursor.fetchone()
        print("Case :", TestData)
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")