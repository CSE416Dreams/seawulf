import json

ms = 0
ga = 0
mKey = {}
gKey = {}


# Need to add Fl as well, but need to create the party [ercentage for it first]

with open("../ms-county-party-percentage.json") as f:
    ms = json.load(f)

with open("../ga-county-party-percentage.json") as f:
    ga = json.load(f)

i = 1
for k,v in ms.items():
    mKey[k] = i
    i += 1

i = 1
for k,v in ga.items():
    gKey[k] = i
    i += 1

with open("msKeys.json", 'w') as f:
    f.write(json.dumps(mKey))

with open("gaKeys.json", 'w') as f:
    f.write(json.dumps(gKey))