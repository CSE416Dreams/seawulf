import json
import geopandas as gp

pre = gp.read_file('./shp files/msp/ms-pre/ms_2020.shp')
block = gp.read_file('./shp files/msp/ms-block/ms_cvap_2020_bg.shp')

pre["geometry"] = pre.buffer(0)
block["geometry"] = block.buffer(0)

for index, row in pre.iterrows():
    pre.at[index, "uid"] = str(index + 1)

only_pre   = pre[["geometry", "G20PRERTRU", "G20PREDBID", "uid"]]
only_pre   = only_pre.rename(columns={'G20PRERTRU':'rep', 'G20PREDBID':'dem'}) 
only_block = block[["geometry", "CVAP_TOT20", "CVAP_ASN20", "CVAP_BLK20", "CVAP_WHT20", "CVAP_HSP20"]]

joined_file = only_block.sjoin(only_pre, predicate="intersects")
#print(joined_file.head())
join = {}
for index, row in joined_file.iterrows():
    if not row["uid"] in join:
        join[row["uid"]] = {}
        join[row["uid"]]["rep"]    = row["rep"]
        join[row["uid"]]["dem"]    = row["dem"]
        '''
        join[row["uid"]]["otherp"]  = row["G20PRELJOR"]
        join[row["uid"]]["otherp"] += row["G20PREODEL"]
        join[row["uid"]]["otherp"] += row["G20PRESLAR"]
        join[row["uid"]]["otherp"] += row["G20PREGHAW"]
        join[row["uid"]]["otherp"] += row["G20PRECBLA"]
        '''
        if row["rep"] > row["dem"]:
            join[row["uid"]]["voting_history"] = "R"
        else:
            join[row["uid"]]["voting_history"] = "D"
        join[row["uid"]]["district"] = ""
    
    join[row["uid"]]["hispanic"]   = join[row["uid"]].get("hispanic", 0) + row["CVAP_HSP20"]
    join[row["uid"]]["white"]      = join[row["uid"]].get("white", 0) + row["CVAP_WHT20"]
    join[row["uid"]]["asian"]      = join[row["uid"]].get("asian", 0) + row["CVAP_ASN20"]
    join[row["uid"]]["black"]      = join[row["uid"]].get("black", 0) + row["CVAP_BLK20"]
    join[row["uid"]]["population"] = join[row["uid"]].get("population", 0) + row["CVAP_TOT20"]
    join[row["uid"]]["other"]      = join[row["uid"]].get("other", 0) + join[row["uid"]]["population"] - (join[row["uid"]]["black"]+join[row["uid"]]["asian"]+join[row["uid"]]["white"]+join[row["uid"]]["hispanic"])

for index, row in pre.iterrows():
    neighbors = pre[pre.geometry.touches(row['geometry'])].uid.tolist()
    try:
        neighbors = neighbors.remove(row.uid)
        #pre.at[index, "my_neighbors"] = ", ".join(neighbors)
    except:
        #pre.at[index, "my_neighbors"] = ", ".join(neighbors)
        a = 0
    join[row["uid"]]["adjacent_nodes"] = neighbors

with open('./shp files/msp/ms-seawulf.json', 'w') as f:
    json.dump(join, f)
    f.close()