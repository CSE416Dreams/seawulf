import geopandas as gp
import json

toAddFrom = gp.read_file('/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/ga/VTD2020-Shape.shp')
toAddTo = gp.read_file('/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/GA_precincts/GA_precincts16.shp')

gdf = toAddTo.merge(toAddFrom[["DISTRICT", "BIDEN20", "TRUMP20"]], on='DISTRICT')
#print(merged.head())
#print(len(merged.items()))
for index, row in gdf.iterrows():
    gdf.at[index, "uID"] = str(index + 1)
adjList = {}
for index, row in gdf.iterrows():
    neighbors = gdf[gdf.geometry.touches(row['geometry'])].uID.tolist()
    try:
        neighbors = neighbors.remove(row.uID)
        gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
    except:
        gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
    adjList[index + 1] = neighbors
    print(index + 1)


with open('./shp files/gaFinal/adjList.json', 'w') as f:
    json.dump(adjList, f)
    f.close()

gdf.drop('geometry', axis=1).to_csv(r'./shp files/gaFinal/ga.csv')