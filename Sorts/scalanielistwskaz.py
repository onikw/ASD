class Node:
    def __init__(self):
        self.val = None  # przechowywana liczba rzeczywista
        self.next = None  # odsyłacz do nastepnego elementu


nnode5 = Node()
nnode5.val = 11

nnode4 = Node()
nnode4.val = 14
nnode4.next = nnode5

nnode3 = Node()
nnode3.val = 6
nnode3.next = nnode4

nnode2 = Node()
nnode2.val = 3
nnode2.next = nnode3

node5 = Node()
node5.val = 2
node5.next = nnode2

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


def merge(p):
    if p.next==None:
        return p

    q=dziel(p)
    p=merge(p)
    q=merge(q)
    return scal(p,q)



def dziel(p):
    licz=0
    start=p
    while(p.next!=None):
        p=p.next
        licz+=1
    p=start
    licz//=2
    while(licz):
        licz-=1
        p=p.next
    pam=p.next
    p.next=None
    return pam



def scal(p,q):
    if p==None: return q
    if q==None: return p


    if p.val<q.val:
        p.next=scal(p.next,q)
        return p
    q.next=scal(p,q.next)
    return q


wypiszliste(node1)
wypiszliste(merge(node1))