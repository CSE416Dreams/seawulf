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
        f.close()
    os.system("rm test1")
with open("floridaPrecincts.json", "w") as f:
    json.dump(stateKey["florida"], f)
with open("georgiaPrecincts.json", "w") as f:
    json.dump(stateKey["georgia"], f)
with open("mississippiPrecincts.json", "w") as f:
    json.dump(stateKey["mississippi"], f)
