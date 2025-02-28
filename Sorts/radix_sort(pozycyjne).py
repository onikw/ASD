
def ktacyfra(x, k):
    return ((x // (10**(k-1))) % 10)

def counting_sort(A, k):
    n = len(A)
    B = [None] * n
    C = [0] * 10

    for i in range(n):
        ind = ktacyfra(A[i],k)
        C[ind] += 1

    for i in range(1, 10):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        ind = ktacyfra(A[i],k)
        B[C[ind] - 1] = A[i]
        C[ind] -= 1

    for i in range(n):
        A[i] = B[i]

def radix_sort(T):
    maks = max(T)

    k = 1
    while maks>0:
        counting_sort(T, k)
        k+=1
        maks//=10


data = [121, 432, 564, 23, 1, 45, 788]
radix_sort(data)
print(data)
