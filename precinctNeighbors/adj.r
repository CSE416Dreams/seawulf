library(sf)
library(redist)

fl <- st_read("path to shp file")
redist.adjacency(fl)