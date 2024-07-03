from numpy import *
from numpy import random
from scipy.stats import beta

import matplotlib.pyplot as plt
import networkx as nx

from Generate_Initialization import Initialization
from Reciprocity import Reciprocity
from Reputation import Reputation

### This is the main script used to run experiments ###

plt.clf()
plt.rcParams.update({'font.size': 32})

# ----- INITIALIZATION & PLOTTING DEFINITIONS ----- #
N = 20
T = 2500
K = 1000
d = N-2
    
t = linspace(0,T,T+1)
    
r = [1.0,0.0,0.5,0.7]
label = ["Reputation", "Reciprocity", "Stochastic", "Rule-based"]

#r = [0.7]
#label = ["Rule-based"]
lstyle = [":", "--", "-.","-"]
lcolor = ["blue", "green", "magenta", "red"]

# ----- MAIN SCRIPT ----- #
for x in range(len(r)):
    capital = zeros(T+1)
    Capital = zeros(T+1)
    
    print("Now computing for... "+str(label[x]))
    for j in range(K):
        if mod(j,int(K/10)) == 0 and j !=0:
            print("Iteration: ",j)
        H = Initialization(N,d)
        Last_agent = random.randint(N)
        
        # ----- THIS IS THE PARRONDO'S PARADOX ITERATION ----- #
        for i in range(1,T+1):
            agentA = random.randint(N)
            agentB = random.choice(H[agentA])
                
            if r[x] == 0.0:
                Last_agent = Reciprocity(H,agentA,agentB,Last_agent,i)
            elif r[x] == 1.0:
                Reputation(H,agentA,i)
            elif r[x] == 0.5:
                if (random.random() < 0.5):
                    Reputation(H,agentA,i)
                else:
                    Last_agent = Reciprocity(H,agentA,agentB,Last_agent,i)
            else:
                if (beta.mean(H.nodes[agentA]["Alpha"]+1, H.nodes[agentA]["Beta"]+1) > H.nodes[agentA]["Threshold"]):
                    Reputation(H,agentA,i)
                else:
                    Last_agent = Reciprocity(H,agentA,agentB,Last_agent,i)
                    
            for k in range(N):
                capital[i] += H.nodes[k]["Capital"]
            
            H.nodes[k]["Alpha"] = H.nodes[k]["A_scale"]*H.nodes[k]["Alpha"]
            H.nodes[k]["Beta"] = H.nodes[k]["B_scale"]*H.nodes[k]["Beta"]
            
        Capital += capital
    
    print(Capital[T]/(N*K*T))
    plt.figure(1,figsize=(24,16),dpi=300)
    plt.plot(t,Capital/(N*K*T),label=label[x],linestyle=lstyle[x],linewidth=3,color=lcolor[x])

plt.legend(loc="best")

plt.xlabel(r"$t$")
plt.ylabel(r"$\bar{d}(t)$")
plt.xlim(0,T)

plt.grid(False)

#plt.figure("After")
#pos = nx.circular_layout(H)  # Use circular layout
#nx.draw(H, pos, with_labels=True)
#nx.draw(H, with_labels=True)


plt.show()
