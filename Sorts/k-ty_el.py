import random
import math
T=[random.randrange(20) for _ in range(10)]
T=[12, 15, 9, 13, 11, 1, 4, 8, 17, 3]


def partition(T,l,r):
    piwo=T[r]
    i=l-1
    for j in range(l,r):
        if T[j]<piwo:
            i+=1
            T[j],T[i]=T[i],T[j]
    i+=1
    T[i],T[r]=T[r],T[i]
    return i
def selectk(T,l,r,k):
    if l==r:
        return T[l]
    mid=partition(T,l,r)
    if mid==k:
        return T[k]
    elif mid>k:
        return selectk(T,l,mid-1,k)
    else:
        return selectk(T,mid+1,r,k)




print(selectk(T,0,len(T)-1,2))