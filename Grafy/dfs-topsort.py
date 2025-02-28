from collections import deque
def dfs(G, topsort):
    n = len(G)
    parent = [None for v in range(n)]
    visited = [False for v in range(n)]
    def dfs_vis(G, u, topsort):
        print(u)
        visited[u] = True
        for v in G[u]:
            if visited[v] == False:
                visited[v] = True
                parent[u] = v
                dfs_vis(G, v, topsort)
        topsort.append(u)
    for u in range(n):
        if visited[u] == False:
            dfs_vis(G, u, topsort)
    print(topsort)
G = [[1, 2, 3], [2, 3], [3], []]
topsort = deque()
dfs(G, topsort)