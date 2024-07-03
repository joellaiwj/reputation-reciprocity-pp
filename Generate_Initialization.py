from numpy import *
from numpy import random
import networkx as nx

### This script takes in two inputs:
#    N: Number of agents in the network
#    d: Network argument
### The function outputs a graph, G, with properties initialized.

def Initialization(N,d):
    #G = nx.complete_graph(N)
    #G = nx.barabasi_albert_graph(N,m=int(N/2))
    #G = nx.connected_watts_strogatz_graph(N,d,0.5)
    #G = nx.karate_club_graph()
    #G = nx.erdos_renyi_graph(N, 0.75)
    G = nx.random_regular_graph(d,N)
    #N = G.number_of_nodes()
    
    for i in range(N):
        G.nodes[i]["Capital"] = 0
        G.nodes[i]["Gave"] = random.choice(["Yes","No"])
        G.nodes[i]["Alpha"] = 0
        G.nodes[i]["Beta"] = 0
        G.nodes[i]["Receive_Interaction"] = 0
        G.nodes[i]["Gave_Interaction"] = 0
        G.nodes[i]["A_scale"] = random.uniform(0.8,1.0)
        G.nodes[i]["B_scale"] = random.uniform(G.nodes[i]["A_scale"],1)
        
        G.nodes[i]["Threshold"] = random.uniform(0.5,1.0)
        
    return G