import json
import os

states = ["florida", "georgia", "mississippi"]
stateKey = {}

# The Columns of the master files
# "precinct","office","party_detailed","party_simplified","mode","votes","county_name","county_fips","jurisdiction_name",
#"jurisdiction_fips","candidate","district","magnitude","dataverse","year","stage","state","special","writein","state_po","state_fips",
#"state_cen","state_ic","date","readme_check"

for i in states:
    # Some files like florida don't have the precinct states in order, so I will open a file, cat to a new file, thenn loop through that file
    stateKey[i] = {}
    with open("../" + i + "Counties.txt") as f:
        counties = f.readlines()
        for county in counties:
            stateKey[i][county] = {}
            # Make test file with the precinct information of the county
            os.system("bash helper.sh " + i + " " + county)
            with open("test1") as pre:
                precincts = pre.readlines()
                j = 0
                for j in precincts:
                    head = j.split(',')
                    precinct = head[0]
                    print(i, county, precinct)
                    if precinct not in stateKey[i][county]:
                        stateKey[i][county][precinct] = {}
                    stateKey[i][county][precinct][head[2]] = stateKey[i][county][precinct].get(head[2], 0) + int(head[5])
                pre.close()
                '''
                    totalVotes = 0
                    # create a new script that extract all the precincts from the file
                    os.system("bash helpPrecinct.sh " + precinct)
                    with open("test2") as prec:
                        lines = prec.readlines()
                        prec.close()
                    j += len(lines)
                    stateKey[i][county][precinct] = {}
                    for k in lines:
                        line = lines.split()
                        stateKey[i][county][precinct][line[2]] = stateKey[i][county][precinct].get(line[2], 0) + int(line[5])
                        totalVotes += int(line[5])
                    stateKey[i][county][precinct]["total"] = totalVotes
                    '''
                '''
                precincts = pre.readlines()
                j = 0
                while j < len(precincts):
                    head = precincts[j].split(',')
                    precinct = head[0]
                    stateKey[i][county][precinct] = {}
                    totalVotes = 0
                    samePrecinctCount = 1
                    # Find out how many lines the precinct has
                    if len(precincts) < j + 1:
                        break
                    while head[0] == precincts[j + samePrecinctCount]:
                        samePrecinctCount += 1

                    for k in range(j, j + samePrecinctCount):
                        line = precincts[k].split(",")
                        stateKey[i][county][precinct][line[2]] = stateKey[i][county][precinct].get(line[2], 0) + int(line[5])

                    stateKey[i][county][precinct]["total"] = totalVotes

                    j += samePrecinctCount
                pre.close()
            '''
            '''
            with open("test1") as pre:
                precincts = pre.readlines()
                #j = 0
                #while j < len(precincts):
                for j in range(0, len(precincts), 10):
                    head = precincts[j].split(',')
                    precinct = head[0]
                    stateKey[i][county][precinct] = {}
                    totalVotes = 0
                    for k in range(j, j + 10):
                        line = precincts[k].split(",")
                    #while 
                        totalVotes += int(line[5]) # Votes for the precinct
                        #if line[2] == "":
                            #stateKey[i][county][precinct]["other"] = stateKey[i][county][precinct].get("other", 0) + int(line[5]) # Add the party and the votes
                            #continue
                        stateKey[i][county][precinct][line[2]] = stateKey[i][county][precinct].get(line[2], 0) + int(line[5])
                    stateKey[i][county][precinct]["total"] = totalVotes
                    
                pre.close()
                '''
                
        f.close()
    os.system("rm test1")
with open("floridaPrecincts.json", "w") as f:
    json.dump(stateKey["florida"], f)
with open("georgiaPrecincts.json", "w") as f:
    json.dump(stateKey["georgia"], f)
with open("mississippiPrecincts.json", "w") as f:
    json.dump(stateKey["mississippi"], f)
    '''
    content = 0
    with open(str(i + "Master.csv")) as f:
        lines = f.readlines()
        f.close()
    # Every 10 lines there is a new precinct
    #
    for i in range(0, len(lines), 10):
        line = lines[i].split()
        
        for j in range(i, 10)
                county: {
                    precinct: {
                        pop: sum of total votes
                        outcome: R or D
                        repVotes:
                        demVotes:
                        otherVotes:
                        ...

                    }
                    ...
                }
    '''