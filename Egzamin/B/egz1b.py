from egz1btesty import runtests

"""
Wiktor Onik nr. 421716

Podejście brutalne

Liczę tablicę sum prefiksowych,
biorę każy możliwy przedział T[i] ... T[j], j>=i
następnie sortuje liczby w tym przedziale, od sumy na danym przedziale odejmuje najwyżej k najmniejszych liczb ujemnych.

Wynik to maksimum z wyników po każdym przedziale

Złożoność czasowa:

Trudno mi ją określić w tym przypadku,
sądzę że to O(n*n*nlog) jednak w praktyce algorytm działa dość szybko gdyż zagnieżdżone pętle są od siebie zalezne


"""


def kstrong(T, k):

    n = len(T)

    maks = 0
    S = [0] * n
    S[0] = T[0]
    for i in range(1, n):
        S[i] = S[i - 1] + T[i]

    maks = 0

    for j in range(0, n):
        wyn = S[j]
        P = T[0 : j + 1]
        P.sort()
        for ite in range(k):
            if j >= ite and P[ite] < 0:
                wyn -= P[ite]
            else:
                break
        maks = max(maks, wyn)

    for i in range(1, n):
        for j in range(i + k - 1, n):
            wyn = S[j] - S[i - 1]
            P = T[i : j + 1]
            P.sort()
            for ite in range(k):
                if j - i >= ite and P[ite] < 0:
                    wyn -= P[ite]
                else:
                    break
            maks = max(maks, wyn)
    return maks


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)
