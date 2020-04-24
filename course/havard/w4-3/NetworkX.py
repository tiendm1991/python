import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np

N = 20
p = 0.2

def ge_grap(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for n1 in G.nodes():
        for n2 in G.nodes():
            if n1 < n2 and bernoulli.rvs(p, p):
                G.add_edge(n1, n2)

a1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
a2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
G1 = nx.to_networkx_graph(a1)
G2 = nx.to_networkx_graph(a2)

gen = nx.connected_components(G1)

LCC1 = max(nx.connected_components(G1), key=len)
LCC2 = max(nx.connected_components(G2), key=len)

print(len(LCC1))
print(len(LCC2))

