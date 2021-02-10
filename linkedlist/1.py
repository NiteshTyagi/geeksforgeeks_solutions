class Node:
    def __init__(self,val=False):
        self.val = val
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def pushFront(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def pushEnd(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            return 

        ptr  = self.head
        while ptr:
            prev = ptr
            ptr = ptr.next
        prev.next = node
        
    def printList(self):
        ptr = self.head
        while ptr:
            print(ptr.val,'--->',end='')
            ptr = ptr.next
        print(ptr,end='\n')

if __name__ == "__main__":

    ll1 = Linklist()
    ll1.pushEnd(1)
    ll1.pushFront(3)
    ll1.pushFront(5)
    ll1.pushEnd(7)
    ll1.pushEnd(3)
    ll1.pushEnd(6)
    ll1.pushFront(2)

    ll1.printList()