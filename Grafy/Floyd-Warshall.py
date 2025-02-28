#Floyd-Warshall
#O(V^3)
#relaksuje po kolei każde połączenie między x i y robi to k razy
def mgarf(E):
    n = 0
    for a, b, _ in E:
        n = max(n, a, b)
    n += 1
    inf = float('inf')
    G = [[inf for _ in range(n)] for _ in range(n)]
    for e in E:
        a, b, w = e
        G[a][b] = w
    return G
def Floy_Wars(G):
    n = len(G)
    inf = float('inf')
    dist = [[0 for _ in range(n)] for _ in range(n)]
    par = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = G[i][j]
                par[i][j] = i
    for k in range(n):
        for x in range(n):
            for y in range(n):
                if dist[x][y] > dist[x][k] + dist[k][y]:
                    dist[x][y] = dist[x][k] + dist[k][y]
                    par[x][y] = par[k][y]
    for k in range(n):
        for x in range(n):
            for y in range(n):
                if dist[x][y] > dist[x][k] + dist[k][y]:
                    dist[x][y] = -inf
                    par[x][y] = -1
    return dist, par
def path(par, a, b):
    def reku(par, a, b, path):
        if a == b:
            return
        reku(par, a, par[a][b], path)
        path.append(b)
    path = [a]
    if par[a][b] == -1 and a != b:
        return None
    reku(par, a, b, path)
    path.reverse()
    return path
E = [
    (0, 1, 5),
    (1, 6, 60),
    (6, 7, -50),
    (7, 8, -10),
    (5, 6, 5),
    (1, 5, 30),
    (5, 8, 50),
    (1, 2, 20),
    (2, 3, 10),
    (3, 2, -15),
    (2, 4, 75),
    (4, 9, 100),
    (5, 4, 25),
]
G = mgarf(E)
distance, parent = Floy_Wars(G)
print(distance[0][8])  # -20
print(path(parent, 0, 8))