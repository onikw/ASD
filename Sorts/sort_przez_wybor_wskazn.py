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



def find_min(p):
    mini = float('inf')
    while p.next!=None:
        if p.next.val<mini:
            mem=p
            mini=p.next.val
        p=p.next
    #end
    result=mem.next
    mem.next=result.next
    return result

def sort(p):
    n=Node()
    n.val=None
    n.next=p
    p=n

    pocz=Node()
    pocz.val=find_min(p).val
    pocz.next=None

    pam=pocz

    while p.next!=None:
        wart=find_min(p)
        pocz.next=wart
        pocz=pocz.next
        pocz.val=wart.val
        pocz.next=None

    return pam
    #end


wypiszliste(sort(node1))
