from egz1atesty import runtests
from queue import PriorityQueue
from math import inf

"""
Wiktor Onik nr. 421716

Obserwacje:
    -nie opłaca nam się brać roweru tak niewygodnego że p>q gdyż wtedy możemy po prostu iść i będzie to szybsze

    -jeśli już dojedziemy do roweru szybkiego(tj. p<q) to nie opłaca nam się z niego zsiadać

    -jeśli weźniemy któryś rower w danym punkcie to ten najszybszy

Pomysł:
    Z danej listy rowerów B zostawiamy jedynie te które są najszybsze w swoim punkcie

    Używając klasycznego algorytmu dijsktry znajdziemy najkrótszy dystan z punktu s do każdego innego,
    oraz z punkut t do każdego innego
    (będziemy więc posiadać dwie tablice dystansów dystA z punktu s i dystB z punktu t).

    Korzystając z powyższych obserwacji nasz wynik to min(dystA(t),distA(i)+dystB(i)*row)
    gdzie i to indeks każdego miasta w którym są rowery "szybkie" a row to "szybkość" czyli  p/q roweru w danym mieście


Złożoność algorytmu:

funkcja krawtosas(G) działa w czasie O(E)
sortowanie na początku O(BlogB) => O(VlogV)
operacje na liście rowerów są w czasie liniowym O(B) => O(V)
algorytm dijkstry działa w czasie O(ElogV)

Ostateczna złożoność czasowa: O(E + VlogV + V + ElogV) => O(ElogV)

"""


def armstrong(B, G, s, t):

    # przekształcam graf G na nG czyli graf sąsiedztwa
    nG = krawtosas(G)
    nGlen = len(nG)

    # sortuje liste wowerów wpierw po indestach aby łatwo usunąć wolniejsze rower z danego miasta
    b = len(B)
    B.sort()

    # filtruje najlepsze rowery w każdym mieście w którym one są
    nr = []
    ind = B[0][0]
    best = B[0][1] / B[0][2]
    bestA = B[0][1]
    bestB = B[0][2]
    for i in range(1, b):
        if B[i] == ind:
            if (B[i][1] / B[i][2]) < best:
                best = B[i][1] / B[i][2]
                bestA = B[i][1]
                bestB = B[i][2]
        else:
            nr.append((ind, bestA, bestB))
            best = B[i][1] / B[i][2]
            ind = B[i][0]
            bestA = B[i][1]
            bestB = B[i][2]

    nr.append((ind, bestA, bestB))

    # tworze tablice bestbikes aby łatwiej sprawdzać czy w danym mieście jest rower i jaką on ma wartość
    bestbike = [inf] * nGlen

    for i in range(b):
        if (
            nr[i][2] > nr[i][1]
        ):  # nie opłaca się brać rowerów tak niewygodnych że szbyciej by było iść
            bestbike[nr[i][0]] = (nr[i][1], nr[i][2])

    # licze dystan od punktu początkowego oraz końcowego
    distA = dijkstra(nG, s)
    distB = dijkstra(nG, t)

    # na pewno Luiza może nie brać roweru i na własnych nonawiązaniugach dobiec
    minw = distA[t]

    # sprawdzam czy wzięcie roweru w danym mieście jest dobrym pomysłem
    for i in range(nGlen):
        if bestbike[i] != inf:
            dist = distA[i] + (distB[i] * bestbike[i][0] / bestbike[i][1])
            minw = min(minw, dist)

    wyn = int(minw)

    return wyn


# funkcja zamienia liste krawedzi na ważony graf sąsiedztwa
def krawtosas(G):
    n = len(G)
    maks = 0
    for i in range(n):
        maks = max(maks, G[i][0], G[i][1])
    nG = [[] for _ in range(maks + 1)]

    for i in range(n):
        u, v, w = G[i][0], G[i][1], G[i][2]
        nG[u].append((v, w))
        nG[v].append((u, w))
    return nG


# klasycznie zaimplementowany algorytm Dijkstry
def dijkstra(G, s):

    n = len(G)

    dist = [inf] * n

    pq = PriorityQueue()
    dist[s] = 0
    pq.put((0, s))

    def Relax(u, v):
        vn, vd = v
        if dist[u] + vd < dist[vn]:
            dist[vn] = dist[u] + vd
            pq.put((dist[vn], vn))

    while not pq.empty():
        _, u = pq.get()
        for v in G[u]:
            Relax(u, v)
    return dist


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
