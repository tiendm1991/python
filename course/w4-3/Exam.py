from collections import Counter
import numpy as np
import pandas as pd


def marginal_prob(chars: dict):
    values = chars.values()
    d = Counter(values)
    s = len(values)
    for k in d:
        d[k] /= s
    return d


def chance_homophily(chars: dict):
    mp = marginal_prob(chars)
    mpValues = np.array(list(mp.values()))
    return sum(mpValues ** 2)


favorite_colors = {
    "ankit": "red",
    "xiaoyu": "blue",
    "mary": "blue"
}

# color_homophily = chance_homophily(favorite_colors)
# print(color_homophily)

df = pd.read_csv("characteristics.csv", low_memory=False, index_col=0)
df1 = df[df.village == 1]
df2 = df[df.village == 2]
d1 = df1.set_index("pid").T.to_dict()
d2 = df2.set_index("pid").T.to_dict()
sex1 = {k: d1[k]["resp_gend"] for k in d1}
caste1 = {k: d1[k]["caste"] for k in d1}
religion1 = {k: d1[k]["religion"] for k in d1}
sex2 = {k: d2[k]["resp_gend"] for k in d2}
caste2 = {k: d2[k]["caste"] for k in d2}
religion2 = {k: d2[k]["religion"] for k in d2}


def homophily(G, chars, IDs):
    """
    Given a network G, a dict of characteristics chars for node IDs,
    and dict of node IDs for each node in the network,
    find the homophily of the network.
    """
    num_same_ties = 0
    num_ties = 0
    for n1, n2 in G.edges():
        if IDs[n1] in chars and IDs[n2] in chars:
            if G.has_edge(n1, n2):
                num_ties += 1
                if chars[IDs[n1]] == chars[IDs[n2]]:
                    num_same_ties += 1
    return (num_same_ties / num_ties)

# pid1  = pd.read_csv("key_vilno_1.csv")
# pid2 = pd.read_csv("key_vilno_2.csv")
# print(vl1[pid1.index == 100])

import networkx as nx
A1 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno1.csv", index_col=0))
A2 = np.array(pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@adj_allVillageRelationships_vilno2.csv", index_col=0))
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

pid1 = np.array(pd.read_csv("key_vilno_1.csv", dtype=int)['0'])
pid2 = np.array(pd.read_csv("key_vilno_2.csv", dtype=int)['0'])

hsex1 = homophily(G1, sex1, pid1)
hcaste1 = homophily(G1, caste1, pid1)
hreligion1 = homophily(G1, religion1, pid1)
hsex2 = homophily(G2, sex2, pid2)
hcaste2 = homophily(G2, caste2, pid2)
hreligion2 = homophily(G2, religion2, pid2)
print([hsex1, hcaste1, hreligion1, hsex2, hcaste2, hreligion2])
hsex1 = chance_homophily(sex1)
hcaste1 = chance_homophily(caste1)
hreligion1 = chance_homophily(religion1)
hsex2 = chance_homophily(sex2)
hcaste2 = chance_homophily(caste2)
hreligion2 = chance_homophily(religion2)
print([hsex1, hcaste1, hreligion1, hsex2, hcaste2, hreligion2])

