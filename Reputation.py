from numpy import *
from numpy import random
from scipy.stats import beta

### This script comprise one part:
#    Reputation: The Reputation social behavior

def Reputation(G,agentA,t):
    Alpha = G.nodes[agentA]["Alpha"] + 1
    Beta = G.nodes[agentA]["Beta"] + 1
    
    if random.random()<beta.mean(Alpha, Beta):
        G.nodes[agentA]["Capital"] = G.nodes[agentA]["Capital"]+1
    else:
        G.nodes[agentA]["Capital"] = G.nodes[agentA]["Capital"]-2

    