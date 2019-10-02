#import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd



G = nx.Graph()
f = open("/Users/alex/Desktop/School Home Base/Cpts 415/routes.dat", "r")
lines = f.readlines()
airports = []
routes = []
airportsDict = {}
for x in lines:
    arr = x.split(',')
    sourceID = arr[3]
    sourceName = arr[2]
    airports.append(sourceID)
    airportsDict[sourceID] = sourceName
    destID = arr[5]
    destName = arr[4]
    if(destName == "BOS" or destName == "SEA"): print(destName + " " + destID)
    routes.append((sourceID,destID))
    #print(sourceName + " to " + destName)
airportsDeDuped = list(dict.fromkeys(airports))
print(sorted(airportsDeDuped))
G.add_nodes_from(sorted(airportsDeDuped))
G.add_edges_from(routes)
print(type(G.nodes))
sea_2_bos = nx.shortest_path(G,"3448","3577")
randoA = nx.shortest_path(G,"346","3577")
randoB = nx.shortest_path(G,"3460","3577")
print(sea_2_bos)
print(randoA)
print(randoB)



