class Node:
    def __init__(self,val=None,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def pushFront(self,val:int):
        node = Node(val)

        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev  = node
        
        self.head = node
        return node



    def pushEnd(self,val:int):
        node = Node(val)
        
        if not self.head:
            node.prev = None
            self.head = node
        else:
            temp = self.head
            while temp and temp.next:
                temp = temp.next
            node.prev = temp
            temp.next = node
        return node
    

    def pushBeforenode(self,val,next_node):
        node = Node(val)
        if next_node is None:
            print('<----- No node exist in Linked List ----->')
            return
        prev_node = next_node.prev
        if prev_node:
            prev_node.next = node
            node.prev = prev_node
            node.next = next_node
            next_node.prev = node
            return node
        else:
            node.prev = None
            node.next = next_node
            next_node.prev = node
            self.head = node
            return node
        

    def pushAfternode(self,val,prev_node):
        node = Node(val)
        if prev_node is None:
            print('<----- No node exist in Linked List ----->')
            return

        node.next = prev_node.next
        node.prev = prev_node
        prev_node.next = node
        if prev_node.next:
            prev_node.next.prev = node

        return node

    def printList(self):
        if self.head:
            temp = self.head
            while temp and temp.next:
                print(temp.val,end=' ---> ')
                temp = temp.next
            print(temp.val,end='\n')
        else:
            print('---- List is empty-----')


if __name__ == '__main__':

    dl = DoublyLinkedList()
    dl.pushFront(3)
    dl.pushFront(4)
    dl.pushFront(2)
    dl.pushFront(5)

    dl.printList()

    dl.pushEnd(10)
    afternode = dl.pushEnd(7)
    beforenode = dl.pushEnd(9)

    dl.printList()

    dl.pushAfternode(19,afternode)

    dl.printList()

    dl.pushBeforenode(21,beforenode)

    dl.printList()
