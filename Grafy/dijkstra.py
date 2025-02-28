#Dijkstra
#O(ElogV)
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
def dijkstra(G, s):
    # inicjalizacja
    n = len(G)
    inf = float('inf')
    par = [None] * n
    dist = [inf] * n
    pq = PriorityQueue()
    dist[s] = 0
    pq.put((0, s))
    def Relax(u, v):
        vn, vd = v
        if dist[u] + vd < dist[vn]:
            dist[vn] = dist[u] + vd
            par[vn] = u
            pq.put((dist[vn], vn))
    # relaksacja
    while not pq.empty():
        _, u = pq.get()
        for v in G[u]:
            Relax(u,v)
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
dijkstra(G, 1)