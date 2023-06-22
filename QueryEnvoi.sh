#!/bin/bash
# Variables de connexion à la base de données

db_host="localhost"
db_user="adminsae24"
db_password="passroot"
db_name="sae24"

# Fonction pour exécuter les commandes MySQL
execute_mysql() {
  query="$1"
  echo "$query" | mysql -h "$db_host" -P "3306" -u "$db_user" -p"$db_password" "$db_name"
}

# Sending the data into the database
INSERT="INSERT INTO \`For_ws\` (\`Num_case\`)  VALUES ($1);"
result=$(execute_mysql "$INSERT")

echo "Envoyé!"