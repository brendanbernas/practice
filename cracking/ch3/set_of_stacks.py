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

class MyBitMap(BitMap):
    """
    Extended BitMap to also find first set bit and dynamically extend its 
    size
    """
    def firstSet(self):
        """Get index of first set bit"""
        if self.count == 0:
            return None
        for i in xrange(self.size()):
            if self.test(i):
                return i

    def set(self, pos):
        """
        Set bit a specified position (index based)
        If position is out of bounds, double size of the underlying bitmap 
        aaray until it is in bounds.
        """
        while pos >= self.size():
            self.bitmap.extend([0 for i in xrange(len(self.bitmap))])

        return super(MyBitMap, self).set(pos)

class SetOfStacks:
    def __init__(self, max=5):
        # start with a single stack
        self._data = []
        self._initMax = max
        self._topSubStackIndex = 0
        # set bits indicate there is space the specified index
        self._bitmap = MyBitMap(max)

    def _createSubStack(self):
        self._data.append(SimpleStack())

    def _getSubStack(self, index):
        return self._data[index]

    def push(self, element):
        # Find appropriate sub stack
        index = self._bitmap.firstSet()
        if index is None:
            # stacks are full, create a new one
            self._createSubStack()
            index = len(self._data) - 1
            self._bitmap.set(index)

        stack = self._getSubStack(index)
        stack.push(element)

        # Is the sub-stack now full?
        if stack.size == self._initMax:
            self._bitmap.reset(index)

    def _doPop(self, index):
        stack = self._getSubStack(index)
        out = stack.pop()
        self._bitmap.set(index)
        return out
    
    def _getTop(self):
        for i in reversed(range(len(self._data))):
            stack = self._getSubStack(i)
            if stack.size > 0:
                return i

    def pop(self):
        index = self._getTop()
        if index is None:
            raise ValueError('Entire stack is empty')

        return self._doPop(index)

    def popAt(self, index):
        """Pop at specified index of sub-stack"""
        top = self._getTop()
        if not top or top < index:
           raise ValueError('Sub-stack does not exist') 
            
        if self._getSubStack(index).size == 0:
            raise ValueError('Sub-stack is empty')
        
        return self._doPop(index)

    def __repr__(self):
        out = StringIO()
        i = 0
        for subStack in self._data:
            if subStack.size:
                out.write(`i` + ': ' + repr(subStack) + '\n')
                i += 1
        return out.getvalue()[:-1]
