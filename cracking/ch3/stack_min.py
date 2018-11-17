# Implementation of Q2, a stack that keeps track of min element
# operations push, pop, and min should all operate in O(1)

# data -> [3, 5, 2, 3, 1]
# 
# min_stack -> [3, 2, 1]
# 
from StringIO import StringIO

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class StackMin():    
    def __init__(self):
        self._data = None
        self._min_data = None
    
    def push(self, element):
        new = Node(element)
        new.next = self._data
        self._data = new

        if self._min_data and self._min_data.value >= element:
            min_new = Node(element)
            min_new.next = self._min_data
            self._min_data = min_new
        elif not self._min_data:
            # initial value for min
            self._min_data = Node(element)
    
    def pop(self):
        if not self._data:
            raise ValueError('Stack is empty')

        out = self._data.value
        self._data = self._data.next

        if out == self.min():
            self._min_data = self._min_data.next

        return out

    def peek(self):
        if not self._data:
            raise ValueError('Stack is empty')
        
        return self._data.value

    def min(self):
        if not self._min_data:
            raise ValueError('Stack is empty')
        
        return self._min_data.value

    def __repr__(self):
        out = StringIO()
        curr = self._data
        while curr:
            out.write(repr(curr.value) + " - ")
            curr = curr.next
        return out.getvalue()[:-3] + ' ]'

    def _min(self):
        """Helper to view internal stack tracking min values"""
        out = StringIO()
        curr = self._min_data
        while curr:
            out.write(repr(curr.value) + " - ")
            curr = curr.next
        return out.getvalue()[:-3] + ' ]'

