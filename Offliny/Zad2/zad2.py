"""
Wiktor Onik

W algorytmie najpierw sortję p pierwszych elementów,
następnie dodaje do wynik wartość k-tego elementu,
potem usuwa z tyłu jeden element i dodaje następny aż do końca tablicy.

Złożoność czasowa plog(p)+(n-p)*p
"""

from zad2testy import runtests

def heapify_max(T,n,ind):
    l=2*ind+1
    r=2*ind+2
    maxind=ind
    if l<n and T[l]>T[maxind]:
        maxind=l
    if r<n and T[r]>T[maxind]:
        maxind=r
    if maxind!=ind:
        T[ind],T[maxind]=T[maxind],T[ind]
        heapify_max(T,n,maxind)

def build_heap_max(T):
    n=len(T)
    p=(n-2)//2
    for i in range(p,-1,-1):
        heapify_max(T,n,i)

def heapsort(T):
    n=len(T)
    build_heap_max(T)
    for i in range (n-1,0,-1):
        T[i],T[0]=T[0],T[i]
        heapify_max(T,i,0)

def ksum(T, k, p):

    tabs=T[:p]
    heapsort(tabs)
    cutind=0
    res=tabs[p-k]
    for i in range(p,len(T)):
        tocut=T[cutind]
        cutind+=1
        start=0
        stop=p-1
        flag=True
        while (start<=stop and flag):
            mid=(start+stop)//2
            if tabs[mid]==tocut:
                flag=False
            elif tabs[mid]>tocut:
                stop=mid-1
            elif tabs[mid]<tocut:
                start=mid+1

        ite=mid
        if tabs[mid]>=T[i]:
            tabs[mid]=T[i]
            while ite-1>=0 and tabs[ite-1] > tabs[ite]:
                tabs[ite],tabs[ite-1]=tabs[ite-1],tabs[ite]
                ite-=1
        else:
            tabs[mid]=T[i]
            while ite+1<p and tabs[ite+1] < tabs[ite]:
                tabs[ite],tabs[ite+1]=tabs[ite+1],tabs[ite]
                ite+=1

        res+=tabs[p-k]

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
