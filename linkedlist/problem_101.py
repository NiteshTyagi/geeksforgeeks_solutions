from problem_1 import Linklist,Node

class Linklist(Linklist):

    def getMiddle(self):
        ptr = self.head
        count=0
        while ptr:
            count+=1
            ptr = ptr.next
        
        return (count//2)
    
    def MiddleToHead(self):
        if not self.head:
            return None
        middle = self.getMiddle()
        
        ptr = self.head
        count = 0
        while ptr:
            if count==middle:
                break
            prev = ptr
            ptr = ptr.next
            count+=1
        
        prev.next = ptr.next
        ptr.next = self.head
        self.head = ptr
        return self.head
        

if __name__ == "__main__":
    #    https://www.geeksforgeeks.org/make-middle-node-head-linked-list/
    ll1 = Linklist()
    ll1.pushEnd(1)
    ll1.pushEnd(2)
    ll1.pushEnd(3)
    ll1.pushEnd(4)
    ll1.pushEnd(5)
    ll1.pushEnd(6)
    
    ll1.printList()
    
    ll1.MiddleToHead()
    
    ll1.printList()