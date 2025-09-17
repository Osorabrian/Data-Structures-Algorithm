class SinglyNode:
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return self.val
        
head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
D = SinglyNode(5)

head.next = A
A.next = B
B.next = C
C.next = D

#display items of a linked list O(n)
def display(head):
    curr = head
    elements = []
    
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
        
    return " -> ".join(elements)

print(display(head))

#seacrh for element in linked list O(n)
def search(val):
    curr = head
    while curr:
        if curr.value == val:
            return True
        curr = curr.next
    return False

print(search(23))

class DoublyNode:

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
    def __str__(self):
        return str(self.value)
    
head = tail = DoublyNode(1)

def display_doubly(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    return " <-> ".join(elements)


def insert_at_beginning(head, tail, value):
    new_node = DoublyNode(value, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
print(display_doubly(head))

def insert_at_end(head, tail, value):
    new_node = DoublyNode(value, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 4)
print(display_doubly(head))