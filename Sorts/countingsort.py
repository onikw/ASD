import random

T = [random.randrange(20) for _ in range(10)]
T = [12, 15, 9, 13, 11, 1, 4, 8, 17, 3]


def counting_sort(A, k):
    n = len(A)
    B = [None] * n
    C = [0] * k

    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]


counting_sort(T, 1000)
print(T)
