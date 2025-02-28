from zad8testy import runtests

"""
Wiktor Onik

Algorytm to iteracyjna implementacja rekurencyjnego wzoru podanego w podpowiedzi do zadania

Gdzie F[i][j] oznacza sume dystansów licząc od 0 do i-tego bloku , i-ty blok może mieć maksymalnie j-ty parking

"""


def parking(X, Y):

    inf = float("inf")

    n = len(X)
    m = len(Y)

    F = [[inf for _ in range(m)] for _ in range(n)]

    F[0][0] = abs(X[0] - Y[0])

    for i in range(1, n):
        F[0][i] = min(abs(X[0] - Y[i]), F[0][i - 1])

    for i in range(1, n):
        for j in range(i, m):
            F[i][j] = min(F[i][j - 1], abs(X[i] - Y[j]) + F[i - 1][j - 1])

    return F[n - 1][m - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
