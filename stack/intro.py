"""
    Stack is a linear data structure that operates on the LIFO (last in first out) principle.
    LIFO principle means that the last element pushed into the array will be the first to come out.

    Type of Stack:
    a) fixed size stack - has a predefined capacity.
    b) Dynamic size stack - can grow and shrink as needed.
    
    Common Operations
    push() - insert an element to the stack
    pop() - remove an element from the stack
    top() - returns the top element of the stack
    isEmpty() - return true if the stack is empty else False
    size() - returns the capacity or length of the stack
"""

# vvariable size
class Stack:
    
    def __init__(self):
        self.arr = []
        
    def push(self, val):
        self.arr.append(val)
        
    def pop(self):
        return self.arr.pop()
    
    def top(self):
        return self.arr[-1]
    
    def is_empty(self):
        if len(self.arr) == 0:
            return True
        return -1
    
    def size(self):
        return len(self.arr)
    
    def get(self):
        return self.arr
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.top())
print(stack.get())
print(stack.size())

print(stack.pop())
print(stack.pop())

print(stack.get())

stack.pop()
stack.pop()

print(stack.is_empty())


