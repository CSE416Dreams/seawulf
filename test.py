import networkx as nx
import pandas as pd
from osgeo import ogr

G = nx.read_shp("./shp/ms_2020/ms_2020.shp")
A = pd.to_pandas_adjacency(G)
print(nx.adjacency_matrix(G))