import json

files = ["florida"]#, "mississippi", "georiga"]
data = None
# Add a "total" value to it
for i in files:
    data = json.load(open(i + "Precincts.json"))
    for county, precincts in data.items():
        for precinct, parties in precincts.items():
            totalVotes = 0
            for party, votes in parties.items():
                totalVotes += votes
            precincts[precinct]["population"] = totalVotes
print(data)