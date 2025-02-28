def mosty(G):
    n = len(G)
    low = [0] * n
    d = [0] * n
    parent = [-1] * n
    preord = 0

    def dfs(u):
        nonlocal preord
        preord += 1
        low[u] = d[u] = preord
        for v in G[u]:
            if d[v] == 0:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])  # updatuje low jak natrafiłem na cykl
            elif v != parent[u]:
                low[u] = min(low[u], d[v])  # updatuje low jak natrafiłem na cykl

    dfs(0)
    for i in range(n):
        if parent[i] != -1 and d[i] == low[i]:
            print("most między", parent[i], "a", i)
    return d, low, parent


G = [[1, 3], [0, 2], [1, 3, 5], [0, 2, 4], [3], [2, 6, 7], [5, 7], [5, 6]]
d, low, parent = mosty(G)
print(d, low, parent)
