# Q4 Implement a MyQueue class which implements a queue using two stacks.

from simple_stack import SimpleStack

class MyQueue():
    def __init__(self):
        # create our two stacks
        self._data = SimpleStack()
        self._temp = SimpleStack()

    def add(self, element):
        self._data.push(element)
    
    def remove(self):
        if self._data.size == 0:
            raise ValueError('Queue is empty')

        # first in our queue is last in our _data stack
        # reverse our queue by sticking it into a temporary stack
        while self._data.size > 0:
            self._temp.push(self._data.pop())