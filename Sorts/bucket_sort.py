import random

T = [random.randrange(20) for _ in range(10)]
T = [12, 15, 9, 13, 11, 1, 4, 8, 17, 3]


def selsort(A):
    n = len(A)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if A[min_ind] > A[j]:
                min_ind = j
        A[i], A[min_ind] = A[min_ind], A[i]


def bucket_sort(T):
    l = len(T)
    A = [[] for _ in range(l)]
    for el in T:
        i = int(el * l / (max(T) + 1))
        A[i].append(el)

    T.clear()

    for i in range(l):
        selsort(A[i])
        T.extend(A[i])


print(T)
bucket_sort(T)
print(T)
