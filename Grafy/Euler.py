from collections import deque
def dfs(G, euler):
    n = len(G)
    visited = [[False] * n for _ in range(n)]
    def dfs_vis(G, u, euler):
        for v in G[u]:
            if visited[v][u] == False:
                visited[v][u] = True
                visited[u][v] = True
                dfs_vis(G, v, euler)
        euler.append(u)
    dfs_vis(G, 0, euler)
    print(euler)
G = [[1, 4], [0, 2, 3, 4], [1, 3], [1, 2, 4, 5], [0, 1, 3, 5], [4, 3]]
euler = deque()
dfs(G, euler)