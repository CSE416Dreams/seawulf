from csv import DictReader
import json
import operator

csvPath = './shp files/ga_2020/ga_2020.csv'
adjPath = './shp files/ga_2020/adjList.txt'
csv = 0
adj = 0
seawulfInput = {}

with open(adjPath) as file:
    adj = file.readlines()
    file.close()

with open(csvPath, 'r') as file:
    csv = DictReader(file)
    i = 0
    for row in csv:
        seawulfInput[i + 1] = {}
        # The following adds the adjacenct Nodes
        adjText = adj[i].strip()
        adjNodes = ""
        if adjText != "c()":
            adjNodes = adjText[2:len(adjText) - 1].split(', ')
        seawulfInput[i + 1]["adjacent_nodes"] = adjNodes
        candidateVotes = {}
        for candidate, votes in row.items():
            if candidate.startswith("G20PRE"):
                candidateVotes[candidate] = int(votes)
        population = sum(candidateVotes.values())
        winningCandidate = max(candidateVotes.items(), key=operator.itemgetter(1))[0]
        votingHistory = ""
        if winningCandidate == "G20PRERTRU":
            votingHistory = "R"
        else:
            votingHistory = "D"
        seawulfInput[i + 1]["population"] = population
        seawulfInput[i + 1]["voting_history"] = votingHistory
        seawulfInput[i + 1]["dem_votes"] = candidateVotes["G20PREDBID"]
        seawulfInput[i + 1]["rep_votes"] = candidateVotes["G20PRERTRU"]
        seawulfInput[i + 1]["district"] = "To be Assigned"
        i += 1
    file.close()

with open('./shp files/ga_2020/ga-seawulf.json', 'w') as f:
    json.dump(seawulfInput, f)