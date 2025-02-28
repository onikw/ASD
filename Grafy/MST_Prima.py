from queue import PriorityQueue
#O(ElogV)
#jakby dijkstra ale zamiast odległości od s po prostu patrzysz na wage danej krawędzi
#do dupy
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
def Prima(G):
    start = 0
    inf = float('inf')
    n = len(G)
    dist = [inf for _ in range(n)]
    par = [None for _ in range(n)]
    dist[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        _, u = pq.get()
        for v, w in G[u]:
            if w < dist[v] and par[u] != v:
                dist[v] = w
                par[v] = u
                pq.put((dist[v], v))
    return par, dist
E = [
    (0, 1, 9),
    (1, 4, 3),
    (4, 6, 6),
    (6, 5, 1),
    (5, 2, 6),
    (2, 0, 0),
    (0, 5, 7),
    (0, 3, 5),
    (3, 5, 2),
    (3, 1, -2),
    (3, 6, 3),
]
G = mgraf(E)
par, dist = Prima(G)
print(dist)