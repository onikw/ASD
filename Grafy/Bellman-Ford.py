      #Bellman-Ford
#O(V^2E)
from queue import PriorityQueue
def mgraf(L):
    n = len(L)
    maks = 0
    for i in range(n):
        x, y, z = L[i]
        maks = max(maks, x, y)
    G = [[] for _ in range(maks + 1)]
    for i in range(n):
        u, v, w = L[i]
        G[u].append((v, w))
        G[v].append((u, w))
    return G
def bellford(G, s):
    # inicjalizacja
    n = len(G)
    inf = float('inf')
    dist = [inf] * n
    par = [None] * n
    dist[s] = 0
    def Relax(u, v):
        vn, vd = v
        if dist[u] + vd < dist[vn]:
            dist[vn] = dist[u] + vd
            par[vn] = u
    # relaksacja
    for i in range(n - 1):
        for u in range(n):
            for v in G[u]:
                Relax(u, v)
    # sprawdzaniacja( jak jest źle to znaczy że cykl ujemny)
    check = True
    for u in range(n):
        for v in G[u]:
            vn, vd = v
            if dist[u] + vd < dist[vn]:
                check = False
    if check == True:
        print(dist[5])
E = [
    (0, 1, 5),
    (1, 2, 21),
    (1, 3, 1),
    (2, 4, 7),
    (3, 4, 13),
    (3, 5, 16),
    (4, 6, 4),
    (5, 6, 1),
]
G = mgraf(E)

bellford(G, 1)