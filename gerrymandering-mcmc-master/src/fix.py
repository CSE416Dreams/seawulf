import json
a = {}
with open('./ga-back.json') as f:
    a = json.load(f)
    f.close()

for i in a:
    a[i]["district"] = ""

b = set()

for i in a:
    if len(b) >= 13:
        break
    for j in a[i]["adjacent_nodes"]:
        b.add(int(j))

count = 1
for i in b:
    a[str(i)]["district"] = str(count)
    count += 1

with open('./ga.json', 'w') as f:
    json.dump(a, f)
    f.close()