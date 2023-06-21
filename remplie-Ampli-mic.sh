#!/bin/bash

# Variables de connexion à la base de données
db_user="adminsae24"
db_password="passroot"
db_name="sae24"
db_host="localhost"

# Fonction pour exécuter les commandes MySQL
execute_mysql() {
  query="$1"
  echo "$query" | /opt/lampp/bin/mysql -N -h "$db_host" -u "$db_user" -p"$db_password" "$db_name"
}

# Récupérer le numéro de cas et les valeurs des AMic1BG, AMic2HG et AMic3HD de la table Coord-Mic
query="SELECT Num_case, AMic1BG, AMic2HG, AMic3HD FROM \`Coord-Mic\`"
result=$(execute_mysql "$query")

# Parcourir les résultats
while IFS=$'\t' read -r numCase ampMic1BG ampMic2HG ampMic3HD; do
  # Récupérer le code binaire correspondant à AMic1BG
  query="SELECT cd_binaire FROM \`Code-binaire\` WHERE Amplitude = '$ampMic1BG'"
  codeMic1BG=$(execute_mysql "$query")

  # Récupérer le code binaire correspondant à AMic2HG
  query="SELECT cd_binaire FROM \`Code-binaire\` WHERE Amplitude = '$ampMic2HG'"
  codeMic2HG=$(execute_mysql "$query")

  # Récupérer le code binaire correspondant à AMic3HD
  query="SELECT cd_binaire FROM \`Code-binaire\` WHERE Amplitude = '$ampMic3HD'"
  codeMic3HD=$(execute_mysql "$query")

  # Afficher le numéro de cas, les valeurs des AMic1BG, AMic2HG, AMic3HD et les codes binaires correspondants
  echo "Num_case: $numCase"
  echo "AMic1BG: $ampMic1BG, Code binaire: $codeMic1BG"
  echo "AMic2HG: $ampMic2HG, Code binaire: $codeMic2HG"
  echo "AMic3HD: $ampMic3HD, Code binaire: $codeMic3HD"
  echo "--------------------------------------"
  
  execute_mysql "INSERT INTO \`Ampli-mic\` (\`Num_case\`, \`cdMic1BG\`, \`cdMic2HG\`, \`cdMic3HD\`)  VALUES ($numCase, '$codeMic1BG', '$codeMic2HG', '$codeMic3HD');"
done <<< "$result"
