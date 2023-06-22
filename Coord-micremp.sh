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

numRows=16
numCols=16
caseWidth=0.5
caseHeight=0.5
mic1X=0.25
mic1Y=0.25
mic2X=0.25
mic2Y=7.75
mic3X=7.75
mic3Y=7.75

calculateDistance() {
  local x1=$1
  local y1=$2
  local x2=$3
  local y2=$4
  local distance=$(bc -l <<< "sqrt(($x2 - $x1)^2 + ($y2 - $y1)^2)")
  echo "$distance"
}

# Remplir les tables Coord-Mic et Ampli-Mic
for ((col=0; col<numCols; col++))
do
  for ((row=0; row<numRows; row++))
  do
    numCase=$((col * numRows + row + 1))
    y=$(bc -l <<< "($caseWidth * $col) + ($caseWidth / 2)")
    x=$(bc -l <<< "($caseHeight * $row) + ($caseHeight / 2)")
    dMicHG=$(calculateDistance "$mic1X" "$mic1Y" "$x" "$y")
    dMicHD=$(calculateDistance "$mic2X" "$mic2Y" "$x" "$y")
    dMicBG=$(calculateDistance "$mic3X" "$mic3Y" "$x" "$y")

    # Vérifier si la distance est nulle pour éviter une division par zéro
    if (( $(echo "$dMicHG == 0" | bc -l) )); then
      ampMicHG="885.41"
    else
      k=$(echo "8.854187 " | bc -l)
      ampMicHG=$(echo "scale=4; $k / ($dMicHG * $dMicHG)" | bc -l)
    fi

    if (( $(echo "$dMicHD == 0" | bc -l) )); then
      ampMicHD="885.41"
    else
      k=$(echo "8.854187" | bc -l)
      ampMicHD=$(echo "scale=4; $k / ($dMicHD * $dMicHD)" | bc -l)
    fi

    if (( $(echo "$dMicBG == 0" | bc -l) )); then
      ampMicBG="885.41"
    else
      k=$(echo "8.854187" | bc -l)
      ampMicBG=$(echo "scale=4; $k / ($dMicBG * $dMicBG)" | bc -l)
    fi

    execute_mysql "INSERT INTO \`Coord-Mic\` (\`Num_case\`, \`x\`, \`y\`, \`Dmic1BG\`, \`Dmic2HG\`, \`Dmic3HD\`, \`AMic2HG\`, \`AMic3HD\`, \`AMic1BG\`)  VALUES ($numCase, $x, $y, $dMicHG, $dMicHD, $dMicBG, $ampMicHD, $ampMicBG, $ampMicHG);"
  done
done

echo "Le remplissage des tables Coord-Mic et Ampli-Mic est terminé."
