import geopandas as gp
import json
files = ['fl']#, 'ga', 'ms']

for i in files:
    fileToWrite = \
        '/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/ga/adjList.json'
    gdf = gp.read_file('/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/ga/VTD2020-Shape.shp')
    # Add ids to the
    for index, row in gdf.iterrows():
        gdf.at[index, "uID"] = str(index + 1)
    #gdf["geometry"] = gdf.buffer(0)
    adjList = {}
    with open(fileToWrite, 'w') as file:
        for index, row in gdf.iterrows():
            neighbors = gdf[gdf.geometry.touches(row['geometry'])].uID.tolist()
            try:
                neighbors = neighbors.remove(row.uID)
                gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
            except:
                gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
            #n = ", ".join(neighbors)
            #n = "c(" + n + ")\n"
            print("Doing precinct {0}".format(index + 1))
            #print(neighbors)
            adjList[index + 1] = neighbors
            #file.write(n)
        json.dump(adjList, file)
        file.close()

#with open(fileToWrite, 'w') as file:
    #