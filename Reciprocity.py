from numpy import *
from numpy import random
from scipy.stats import beta

### This script comprise two parts:
#    Ebbinghaus: Defines the Ebbinhaus remembering function
#    Reciprocity: The Reciprocity social behavior

def Ebbinghaus(G,agent,t):
    k1 = 1.84
    k2 = 1.25
    dt = t-G.nodes[agent]["Receive_Interaction"]
    return (100*k1)/(((log(dt))**k2)+k1)

def Reciprocity(G,agentA,agentB,Last_agent,t):
    if (Last_agent in G[agentA]) and (random.random()<Ebbinghaus(G,agentA,t)) and (random.random()<Ebbinghaus(G,Last_agent,t)):
        G.nodes[agentA]["Capital"] = G.nodes[agentA]["Capital"]-1
        G.nodes[agentB]["Capital"] = G.nodes[agentB]["Capital"]+1
        G.nodes[agentA]["Gave"] = "Yes"
        G.nodes[agentA]["Alpha"] += 1
        G.nodes[agentB]["Receive_Interaction"] = t
        G.nodes[agentA]["Gave_Interaction"] = t
        Last_agent = agentA
    else:
        G.nodes[agentA]["Capital"] = G.nodes[agentA]["Capital"]-1
        G.nodes[agentA]["Gave"] = "No"
        G.nodes[agentA]["Beta"] += 1
     
    return Last_agent



