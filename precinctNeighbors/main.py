import geopandas as gp
import rtree as rt

file = gp.read_file('../shp/fl_2020/fl_2020.shp')
#for col in file.columns:
#    print(col)

for index, precinct in file.iterrows():
    # get 'not disjoint' countries
    neighbors = file[~file.geometry.disjoint(precinct.geometry)].precinct.tolist()

    # remove own name of the country from the list
    neighbors = [name for name in neighbors if precinct.precinct != name]

    # add names of neighbors as NEIGHBORS value
    file.at[index, "NEIGHBORS"] = ", ".join(neighbors)



