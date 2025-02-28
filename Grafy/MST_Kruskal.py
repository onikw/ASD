#O(ElogV) = O(ElogE)
#sortuje Edges i wybiera n-1 najmknijeszych nie będących w cyklu
#co sprawdzamy przy użyciu find-union
class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    elif x.rank < y.rank:
        x.parent = y
    else:
        x.parent = y
        y.rank += 1
def sortEdg(E):
    E.sort(key=lambda x: x[2])
    return E
#E graf w postacie połączen
#G normalny listy sasiedztwa
def Kruskal(G, E):
    E = sortEdg(E)
    n = len(G)
    nodyw = [Node(v) for v in range(n)]
    drz = []
    for edge in E:
        u, v, w = edge
        kou, kov = find(nodyw[u]), find(nodyw[v])
        if kou != kov:
            union(kou, kov)
            drz.append(edge)
    return drz