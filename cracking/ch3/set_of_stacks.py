# Q3
# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.

# TODO is this how we want to implement this substack?
# OPTION1: we can implement them with an array with an explicit size
# -> has built in size
# OPTION2: use a linked list, no built in size
# -> will have to create some sort of way to hold size

from StringIO import StringIO
from bitmap import BitMap
from simple_stack import SimpleStack

class Node():
    "Simple node for a linked list"
    def __init__(self, value):
        self.value = value
        self.next = None

class SetOfStacks:
    def __init__(self, max=5):
        # start with a single stack
        self._data = []
        self._createSubStack()
        self._initMax = max
        self._topSubStackIndex = 0  # index for top sub stack

    def _createSubStack(self):
        self._data.append(SimpleStack())

    def _getSubStack(self, index):
        return self._data[index]

    def push(self, element):
        # Is top stack full?
        if self._getSubStack(self._topSubStackIndex).size == self._initMax:
            # make new sub stack, index +1
            self._createSubStack()
            self._topSubStackIndex += 1
        
        stack = self._getSubStack(self._topSubStackIndex)
        stack.push(element)

    def pop(self):
        # curr top substack empty
        if self._getSubStack(self._topSubStackIndex).size == 0:
            if self._topSubStackIndex == 0:
                raise ValueError('Stack is empty')
            self._bitmap.set(_topSubStackIndex)
            self._topSubStackIndex -= 1
        
        return self._getSubStack(self._topSubStackIndex).pop()

    def popAt(self, index):
        """Pop at specific index"""
        # todo lets build a bitmap which will decide which queue to push to next
        pass

    def __repr__(self):
        out = StringIO()
        i = 0
        for subStack in self._data:
            if subStack.size:
                out.write(`i` + ': ' + repr(subStack) + '\n')
                i += 1
        return out.getvalue()[:-1]
            