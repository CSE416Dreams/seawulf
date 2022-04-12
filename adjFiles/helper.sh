
# Helps with the parserMaster.py
cat $1Master.csv | awk -F ',' -v county="$2" '$7 == county {print}' > test1