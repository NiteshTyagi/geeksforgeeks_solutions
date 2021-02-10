from problem_1 import Linklist,Node

class Linklist(Linklist):

    def CountRotation(self):
        ptr = self.head
        countRotation = 1
        while ptr and ptr.next:
            if ptr.next.val > ptr.val:
                countRotation+=1
            else:
                break
            ptr = ptr.next
        return countRotation
    

if __name__ == "__main__":
    #    https://www.geeksforgeeks.org/count-rotations-sorted-rotated-linked-list/

    ll1 = Linklist()
    ll1.pushFront(12)
    ll1.pushFront(11)
    ll1.pushFront(8)
    ll1.pushFront(5)
    ll1.pushFront(18)
    ll1.pushFront(15)
    
    ll1.printList()
    
    print('--countRotation->',ll1.CountRotation())
    
    