
# Helps with the parserMaster.py
cat test1 | awk -F ',' -v precinct="$1" '$1 == precinct {print}' > test2