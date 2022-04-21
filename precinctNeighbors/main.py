import geopandas as gp

files = ['fl', 'ga']
'''
gdf = gp.read_file('/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/fl_2020/fl_2020.shp')
gdf["geometry"] = gdf.buffer(0)
for index, row in gdf.iterrows():
    neighbors = gdf[gdf.geometry.touches(row['geometry'])].pct_std.tolist()
    geoKey[index + 1] = row['pct_std']
    try:
        neighbors = neighbors.remove(row.pct_std)
    except:
        a = 0
    gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
    print(row.pct_std, neighbors)
    '''
for i in files:
    fileToWrite = '/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/{0}_2020/adjList.txt'.format(i, i)
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