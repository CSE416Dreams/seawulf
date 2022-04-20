import geopandas as gp
import rtree as rt

gdf = gp.read_file('../FloridaPrecinctswithElectionData.geojson')
print(gdf.head())

for index, row in gdf.iterrows():
    neighbors = gdf[gdf.geometry.touches(row['geometry'])].name.tolist()
    neighbors = neighbors.remove(row.name)
    gdf.at[index, "my_neighbors"] = ", ".join(neighbors)
