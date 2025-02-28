from collections import deque
def transg(G, transG):
    n = len(G)
    for i in range(n):
        for v in G[i]:
            transG[v].append(i)
def SSS(G):
    n = len(G)
    post = 0
    postord = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    transG = [[] for _ in range(n)]
    def dfs(G, u):
        nonlocal post
        visited[u] = True
        for v in G[u]:
            if visited[v] == False:
                dfs(G, v)
        postord[post] = u
        post += 1
    kol = 0
    tkol = [-1 for _ in range(n)]
    def tdfs(tG, u):
        nonlocal kol
        visited[u] = True
        for v in tG[u]:
            if visited[v] == False:
                tdfs(tG, v)
        tkol[u] = kol
    dfs(G, 0)
    transg(G, transG)
    print(postord)
    print(transG)
    for i in range(n):
        visited[i] = False
    for i in range(n - 1, 0, -1):
        if visited[postord[i]] == False:
            tdfs(transG, postord[i])
            kol += 1
    print(tkol)
G = [[1], [2, 5], [3], [0, 8], [5, 7], [6], [4], [6], [9], [10], [6, 11], [8]]
SSS(G)