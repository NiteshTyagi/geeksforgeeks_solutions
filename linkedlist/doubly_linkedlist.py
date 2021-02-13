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
        if prev_node and prev_node.next:
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
        if prev_node.next:
            prev_node.next.prev = node
        prev_node.next = node
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

    def deletionFront(self):
        if not self.head:
            print('<----- DeletionFront Linked List is empty ----->')
        else:
            temp = self.head
            if temp:
                if temp.next:
                    temp.next.prev = None
                    self.head = temp.next
                else:
                    self.head = None
        return self.head

    def deletionEnd(self):
        if not self.head:
            print('<----- DeletionEnd Linked List is empty ----->')
        else:
            temp = self.head
            while temp and temp.next:
                temp = temp.next
            if temp.prev:
                temp.prev.next = None
            else:
                self.head = None
        return self.head

    def deletionBeforeNode(self,after_node):
        if after_node is None:
            print('<----- After Node does not exist ---->')
        else:
            if after_node.prev:
                if after_node.prev.prev:
                    after_node.prev.prev.next = after_node
                else:
                    after_node.prev = None
                    self.head = after_node
            else:
                self.head = None
        return self.head

    def deletionAfterNode(self,before_node):
        if before_node is None:
            print('<----- Before Node does not exist ---->')
        else:
            if before_node.next:
                if before_node.next.next:
                    before_node.next.next.prev = before_node
                    before_node.next = before_node.next.next
                else:
                    before_node.next = None
            else:
                print('-----No node exist after this node-----')
        return self.head
                
                
if __name__ == '__main__':

    dl = DoublyLinkedList()
    dl.pushFront(3)
    dl.pushFront(4)
    dl.pushFront(2)
    dl.pushFront(5)
    dl.printList()

    dl.pushEnd(10)
    afternode = dl.pushEnd(7)
    dl.pushEnd(9)
    dl.printList()

    beforenode = dl.pushAfternode(19,afternode)
    dl.printList()

    dl.pushBeforenode(21,beforenode)
    dl.printList()

    dl.deletionFront()
    dl.deletionEnd()

    dl.deletionBeforeNode(beforenode)
    dl.deletionAfterNode(afternode)
    dl.printList()
