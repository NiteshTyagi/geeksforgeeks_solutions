from problem_1 import Linklist,Node

class Linklist(Linklist):
    
    def CreateLoop(self,n:int):
        ptr = self.head
        count = 0
        while ptr.next:
            if count==n:
                temp = ptr
            count+=1
            ptr = ptr.next
        ptr.next = temp
        return self.head

    def DetectLoop(self):
        slow  = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count=1
                slow = slow.next
                while slow!=fast:
                    count+=1
                    slow = slow.next

                return count
        return False


if __name__ == "__main__":
    #    https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/

    ll1 = Linklist()
    ll1.pushEnd(1)
    ll1.pushEnd(2)
    ll1.pushEnd(3)
    ll1.pushEnd(4)
    ll1.pushEnd(5)
    ll1.pushEnd(6)
    
    ll1.printList()
    ll1.CreateLoop(3)
    print('---Length of Loop in Linked List--',ll1.DetectLoop())
    
    
    
    