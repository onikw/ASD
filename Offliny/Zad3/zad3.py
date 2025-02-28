from zad3testy import runtests
"""
Wiktor Onik

Alogytm o złożoności O(n)

Najpierw zliczam ile punktów na osi y jest >= od indeksu w tablicy
następnie "filtruję" elementy o tej samej współrzednej x, wybierając tą o maks y
bo np jeśli mamy (12,4) i (12,6) to jeśli ktłóryś punkt bd dominował to ten drugi.
teraz idąc od tyłu liczę ile punktów dominuje każdy punkt.
wzór to: wszystkie punkty - punkty nad dany punktem - punkty za lub na równi z nim
niektóre punkty otrzymają zbyt mały wynik pn
       |  y
-------x---
       |
licząc dominacje punktu x odejmimy dwa razy punkt y,
jednak nie przeszkadza to nam pn w takim wypadku x jest podzbiorem y,
wiemy więc że rezultat to potencjalnie wynik z y a napewno nie x.
"""
def dominance(P):
    n=len(P)
    Py=[0 for i in range(n+1)]
    for i in range(n):
        Py[P[i][1]]+=1
    for i in range(n-1,-1,-1):
        Py[i]+=Py[i+1]
    Pm=[(0,0) for i in range (n+1)]
    for i in range(n):
        x,y=P[i]
        maks=max(y,Pm[x][1])
        Pm[x]=(Pm[x][0]+1,maks)
    wyn=0
    pop=0
    for i in range(n,0,-1):

        kan=n-pop-Py[Pm[i][1]]-Pm[i][0]+1
        pop+=Pm[i][0]
        wyn=max(wyn,kan)
    return wyn

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
