import geopandas as gp

files = ['fl', 'ga', 'ms']

for i in files:
    fileToWrite = \
        '/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/{0}_2020/adjList.txt'.format(i, i)
    gdf = gp.read_file(
        '/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/{0}_2020/{1}_2020.shp'.format(i, i))
    # Add ids to the
    for index, row in gdf.iterrows():
        gdf.at[index, "uID"] = str(index + 1)
    gdf["geometry"] = gdf.buffer(0)
    with open(fileToWrite, 'w') as file:
        for index, row in gdf.iterrows():
            neighbors = gdf[gdf.geometry.touches(row['geometry'])].uID.tolist()
            try:
                neighbors = neighbors.remove(row.uID)
                gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
            except:
                gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
            n = ", ".join(neighbors)
            n = "c(" + n + ")\n"
            print("Doing {0} precinct {1}".format(i, index))
            file.write(n)
    file.close()