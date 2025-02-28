"""
Wiktor Onik

Algorytm działa jako hybryda dwóch algorytmów sortowania przez scalanie o złożoności O(nlogn)
oraz sortowania przez wybór z wprowadzoną optymalizacją przeszukiwania jedynie k el. co daje nam złożoność O(nk).

Dla danych z k mniejszym niż logn używam pierwszego algorytmu a pozostałych drugiego.


Dla k = Θ(1) algorytm przymuje złożoność O(nk)
Dla k = Θ(logn) algorytm przymuje złożoność O(nlogn)
Dla k = Θ(n) algorytm przymuje złożoność O(nlogn)

"""

from zad1testy import Node, runtests

def wypnij(p,n_el):
    while(n_el>1):
        n_el-=1
        p=p.next
    p2=p.next
    p.next=None
    return p2


def scal(p,q):
    if p==None: return q
    if q==None: return p


    if p.val<q.val:
        p.next=scal(p.next,q)
        return p
    q.next=scal(p,q.next)
    return q



def merge_sort(p,rozmlisty):
    if(p!=None and p.next!=None):
        pr=merge_sort(wypnij(p,rozmlisty//2),rozmlisty-rozmlisty//2)
        le=merge_sort(p,rozmlisty//2)
        return scal(pr,le)
    return p

def find_min(p,k):
    mini = float('inf')
    licz=0
    while p.next!=None and licz<=k:
        licz+=1
        if p.next.val<mini:
            mem=p
            mini=p.next.val
        p=p.next
    #end
    result=mem.next
    mem.next=result.next
    return result


def SortH(p,k):

    if k==0:
        return p
    rozmlisty=0
    node=p
    while(node!=None):
        rozmlisty+=1
        node=node.next

    if True:
        n=Node()
        n.val=None
        n.next=p
        p=n

        pocz=Node()
        pocz.val=find_min(p,k).val
        pocz.next=None

        pam=pocz

        while p.next!=None:
            wart=find_min(p,k)
            pocz.next=wart
            pocz=pocz.next
            pocz.val=wart.val
            pocz.next=None
        return pam
    else:
        return merge_sort(p,rozmlisty)



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
