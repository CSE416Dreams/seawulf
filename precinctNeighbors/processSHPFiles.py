from csv import DictReader
import json
import operator

csvPath = './shp files/gaFinal/ga.csv'
adjPath = './shp files/ga/adjList.json'
csv = 0
adj = 0
seawulfInput = {}

with open(adjPath) as file:
    adj = json.load(file)
    file.close()

districts = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10, 11, 12, 13, 14]

with open(csvPath, 'r') as file:
    csv = DictReader(file)
    i = 0
    for row in csv:
        seawulfInput[i + 1] = {}
        seawulfInput[i + 1]["adjacent_nodes"] = adj[str(i + 1)]
        '''
        for candidate, votes in row.items():
            if candidate == "BIDEN20":
                seawulfInput[i+1]["dem_votes"] = int(votes)
            if candidate == "TRUMP20":
                seawulfInput[i+1]["rep_votes"] = int(votes)
        '''
        print(i)
        seawulfInput[i+1]["dem_votes"] = int(float(row["BIDEN20"]))
        seawulfInput[i+1]["rep_votes"] = int(float(row["TRUMP20"]))
        seawulfInput[i+1]["black"]     = int(float(row["BVAP"]))
        seawulfInput[i+1]["white"]     = int(float(row["WVAP"]))
        seawulfInput[i+1]["asian"]     = int(float(row["ASIANVAP"]))
        seawulfInput[i+1]["hispanic"]  = int(float(row["HVAP"]))
        seawulfInput[i+1]["other"]  = int(row["OTHERVAP"]) + int(row["NHPIVAP"]) + int(row["2MOREVAP"])
        pop = int(row["BVAP"]) + int(row["WVAP"]) + int(row["ASIANVAP"]) + int(row["HVAP"]) + seawulfInput[i+1]["other"]
        seawulfInput[i+1]["population"] = pop
        seawulfInput[i+1]["district"] = str(districts[(i - 1) % 14])
            
        if seawulfInput[i+1]["dem_votes"] > seawulfInput[i+1]["rep_votes"]:
            seawulfInput[i+1]["voting_history"] = "D"
        else:
            seawulfInput[i+1]["voting_history"] = "R"
        i += 1
        
        '''
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
        '''
    file.close()

with open('./shp files/gaFinal/ga-seawulf.json', 'w') as f:
    json.dump(seawulfInput, f)