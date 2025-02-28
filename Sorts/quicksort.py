import random

T=[random.randrange(20) for _ in range(10)]
T=[12, 15, 9, 13, 11, 1, 4, 8, 17, 3]


def part(T,l,r):
    piv=T[r]
    i=l-1
    for j in range (l,r):
        if T[j]<piv:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[i],T[r]=T[r],T[i]
    return i

def quicksort(T,l,r):
    if l<r:
        m=part(T,l,r)
        quicksort(T,l,m-1)
        quicksort(T,m+1,r)

quicksort(T,0,len(T)-1)

print(T)