class SinglyNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def k_node(head, k):
    counter = 2
    curr = head
    while curr:
        if counter == k:
            curr = curr.next
            counter = 2
        else:
            counter -= 1
        curr = curr.next
    return head    
    
n = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
D = SinglyNode(5)
n.next = A
A.next = B
B.next = C
C.next = D

curr = head
