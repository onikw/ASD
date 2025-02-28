import random
import math
T=[random.randrange(20) for _ in range(10)]
T=[12, 15, 9, 13, 11, 1, 4, 8, 17, 3]


def print_heap(T,n):

    depth=math.ceil(math.log2(n))
    width=2**(depth-2)*5+2**(depth-2)-1
    print(width)
    for i in range(depth):
        wyn=1
        for j in range(depth-2,i-1,-1):
            wyn=2+2*wyn+1
            print(i," ",j," ",wyn)


def heapify(T,n,ind):
    l=2*ind+1
    r=2*ind+2
    maxind=ind
    if l<n and T[l]<T[maxind]:
        maxind=l
    if r<n and T[r]<T[maxind]:
        maxind=r
    if maxind!=ind:
        T[ind],T[maxind]=T[maxind],T[ind]
        heapify(T,n,maxind)

def build_heap(T):
    n=len(T)
    p=(n-2)//2
    for i in range(p,-1,-1):
        heapify(T,n,i)


def heapsort(T):
    n=len(T)
    build_heap(T)
    for i in range (n-1,0,-1):
        T[i],T[0]=T[0],T[i]
        heapify(T,i,0)




print(T)
heapsort(T)
print(T)