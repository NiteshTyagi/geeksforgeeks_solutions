class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None


    def pushFront(self,val:int):
        node = Node(val)
        if self.head:
            temp = self.head
            node.next = self.head
            while (temp.next!=self.head):
                temp = temp.next
            temp.next = node
        else:
            node.next = node
        
        self.head = node
        return self.head

    def pushEnd(self,val:int):
        node = Node(val)
        if not self.head:
            node.next = node
            self.head = node
            return self.head

        temp = self.head
        while(temp.next!=self.head):
            temp = temp.next
        temp.next = node
        node.next = self.head
        return self.head


    def pushAtposition(self,val,position:int):
        node = Node(val)
        if position==0:
            return self.pushFront(val)
            
        count = 0
        temp = self.head
        while(temp.next!=self.head):
            if count==position:
                node.next = temp.next
                temp.next = node
                return self.head
            count+=1
            temp=temp.next

        temp.next = node
        node.next = self.head

        return self.head

    def printCircularList(self):
        if self.head:
            temp = self.head
            while (temp.next!=self.head):
                print(temp.val,'--->',end=' ')
                temp = temp.next
                
            print(temp.val,end='\n')
        return None



if __name__=='__main__':

    cl = circularLinkedList()
    cl.pushFront(3)
    cl.pushFront(5)
    cl.pushFront(2)
    cl.pushFront(1)
    cl.pushFront(6)

    cl.printCircularList()

    cl.pushEnd(7)
    cl.pushEnd(4)
    cl.pushEnd(9)

    cl.printCircularList()

    cl.pushAtposition(10,0)

    cl.printCircularList()
