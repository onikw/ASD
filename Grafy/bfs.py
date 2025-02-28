#BFS
#O(V+E)
from collections import deque
def bfs(G, s):
    n = len(G)
    d = [-1 for v in range(n)]
    visited = [False for v in range(n)]
    parent = [None for v in range(n)]
    q = deque()
    q.append(s)
    d[s] = 0
    visited[s] = True
    while len(q) > 0:
        u = q.popleft()
        print(u)
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                q.append(v)
G = [
    [1, 3],  # Wierzchołek 0 ma sąsiadów 1 i 3
    [0, 2, 3],  # Wierzchołek 1 ma sąsiadów 0, 2 i 3
    [1, 4],  # Wierzchołek 2 ma sąsiadów 1 i 4
    [0, 1],  # Wierzchołek 3 ma sąsiadów 0 i 1
    [2],  # Wierzchołek 4 ma sąsiada 2
]
bfs(G, 0)