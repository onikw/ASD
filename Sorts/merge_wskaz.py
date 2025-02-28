class Node:
    def __init__(self):
        self.val = None  # przechowywana liczba rzeczywista
        self.next = None  # odsyłacz do nastepnego elementu

node5 = Node()
node5.val = 6

node4 = Node()
node4.val = 3
node4.next = node5

node3 = Node()
node3.val = 2
node3.next = node4

node2 = Node()
node2.val = 5
node2.next = node3

node1 = Node()
node1.val = 1
node1.next = node2


def wypiszliste(p):
    while p != None:
        print(p.val, "-> ", end="")
        p = p.next
    print("TYLE")


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

wypiszliste(node1)
merge_sort(node1,5)
wypiszliste(node1)
