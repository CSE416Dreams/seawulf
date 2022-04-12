#!/bin/sh

# Extracts the data for the selected states from the "masterFile"

cat "../2020-PRESIDENT-precinct-general.csv" | awk -F ',' '$17 == "\"FLORIDA\"" {print}' | tr -d '"' > floridaMaster.csv
cat "../2020-PRESIDENT-precinct-general.csv" | awk -F ',' '$17 == "\"MISSISSIPPI\"" {print}' | tr -d '"' > mississippiMaster.csv
cat "../2020-PRESIDENT-precinct-general.csv" | awk -F ',' '$17 == "\"GEORGIA\"" {print}' | tr -d '"' > georgiaMaster.csv