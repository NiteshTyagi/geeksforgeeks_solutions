class Node:
    def __init__(self, val=None:int):
        self.val = val
        self.next = None

def getJosephusPosition(m, n):
    
    head = Node(1)
    prev = head
    for i in range(2, n + 1):
        prev.next = Node(i)
        prev = prev.next
    prev.next = head  # Connect last
    

    
    ptr1 = head
    ptr2 = head
    # print(ptr1.data,ptr2.data,sep='<---111---->')
    while (ptr1.next != ptr1):
        count = 1
        while (count != m):
            ptr2 = ptr1
            ptr1 = ptr1.next
            count += 1

        ptr2.next = ptr1.next
        
        ptr1 = ptr2.next

    print("Last person left standing (Josephus Position) is ", ptr1.data)


if __name__ == '__main__':
    # https://www.geeksforgeeks.org/josephus-circle-using-circular-linked-list/
    n = 14
    m = 2
    getJosephusPosition(m, n)

