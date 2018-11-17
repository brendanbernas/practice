# Simple implementation of a stack to used in other modules
# Uses a linked list

from StringIO import StringIO

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SimpleStack():    
    def __init__(self):
        self._data = None
        self.size = 0
    
    def push(self, element):
        new = Node(element)
        new.next = self._data
        self._data = new
        self.size += 1
    
    def pop(self):
        if not self._data:
            raise ValueError('Stack is empty')

        out = self._data.value
        self._data = self._data.next
        self.size -= 1

        return out

    def peek(self):
        if not self._data:
            raise ValueError('Stack is empty')
        
        return self._data.value

    def __repr__(self):
        out = StringIO()
        curr = self._data
        while curr:
            out.write(repr(curr.value) + " - ")
            curr = curr.next
        return out.getvalue()[:-3] + ' ]'