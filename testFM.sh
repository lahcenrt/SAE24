#!/bin/bash
# Variables de connexion à la base de données
db_host="192.168.195.134"
db_user="adminsae24"
db_password="passroot"
db_name="sae24"



# Fonction pour exécuter les commandes MySQL
execute_mysql() {
  query="$1"
  echo "$query" | mysql -h "$db_host" -P "3306" -u "$db_user" -p"$db_password" "$db_name"
}

# Récupérer la valeur de AMic1BG de la table Coord-Mic
INSERT="INTO \`For_ws\` (\`Num_case\`, \`AMic2HG\`, \`AMic3HD\`, \`AMic1BG\`)  VALUES ($numCase, $alacon, $suspanus);"
result=$(execute_mysql "$INSERT")

# Afficher la valeur de AMic1BG
echo "$result"
