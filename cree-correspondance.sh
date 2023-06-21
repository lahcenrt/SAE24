#!/bin/bash

# Variables de connexion à la base de données
db_user="adminsae24"
db_password="passroot"
db_name="sae24"
db_host="localhost"

# Fonction pour exécuter les commandes MySQL
execute_mysql() {
  query="$1"
  echo "$query" | /opt/lampp/bin/mysql -h "$db_host" -u "$db_user" -p"$db_password" "$db_name"
}

# Récupérer les valeurs de AMic1BG depuis la base de données
result=$(execute_mysql "SELECT AMic1BG FROM \`Coord-Mic\`")

# Vérifier si la requête a réussi
if [ $? -eq 0 ]; then
  # Supprimer les en-têtes de colonnes
  result=$(echo "$result" | tail -n +2)

  # Enregistrer les valeurs dans un fichier CSV avec incrémentation binaire
  output_csv="./output.csv"
  counter=0
  echo "$result" | sort -u | while IFS= read -r line; do
    binary_counter=$(printf "%08d" $(echo "obase=2;$counter" | bc))
    echo "$line,$binary_counter"
    counter=$((counter+1))
  done | awk -F',' 'BEGIN { OFS="," } { print $1, $2 }' > "$output_csv"
  #execute_mysql "INSERT INTO \`Code_binaire\` (\`Ampplitude\`,\`cd_binaire\`) VALUES ($result, $binary_counter);"
  done

  echo "Les valeurs uniques de AMic1BG avec incrémentation binaire ont été enregistrées dans le fichier CSV : $output_csv"
else
  echo "Une erreur s'est produite lors de la récupération des valeurs de AMic1BG."
fi
