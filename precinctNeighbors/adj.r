library(sf)
library(redist)

ga <- st_read("./shp files/ga_2020")
st_write(ga, "/Users/saifulhaque/PycharmProjects/seawulf/precinctNeighbors/shp files/ga_2020/ga_2020.csv")
redist.adjacency(ga)