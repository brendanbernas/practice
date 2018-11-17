# Implemention of Q1, a single array being used for 3 Stacks
from StringIO import StringIO

class ThreeStacks():
    def __init__(self, size=10):
        # triple the size
        self._data = [None] * size * 3
        self._initSize = size
        # keep track of the top of each stack
        self._top1 = -1
        self._top2 = size - 1
        self._top3 = (size * 2) - 1

    def _checkValidStackNum(self, stackNum):
        if stackNum not in (1, 2, 3):
            raise ValueError('Invalid Stack Number {0}'.format(stackNum))
    
    def _getBottomIndex(self, stackNum):
        """Get bottom index of a particular stack in underlying list"""
        return self._initSize * (stackNum - 1)

    def _getTopIndex(self, stackNum):
        """Get top index of a particular stack in underlying list"""
        return getattr(self, '_top{}'.format(stackNum))

    def pop(self, stackNum):
        self._checkValidStackNum(stackNum)
        
        # determine which one we are popping
        top = self._getTopIndex(stackNum)
        
        # detemine if a stack is already empty
        if top < self._getBottomIndex(stackNum):
            raise ValueError('Stack Number {0} is empty'.format(stackNum))

        # move our counter down
        setattr(self, '_top{}'.format(stackNum), top - 1)

        return self._data[top]
    
    def peek(self, stackNum):
        self._checkValidStackNum(stackNum)
        return self._data[self._getTopIndex(stackNum)]

    def push(self, stackNum, value):
        self._checkValidStackNum(stackNum)
        top = self._getTopIndex(stackNum)
        if top - (self._initSize * stackNum) == -1:
            raise ValueError('Stack Number {0} is full'.format(stackNum))

        top += 1
        setattr(self, '_top{0}'.format(stackNum), top)
        self._data[top] = value

        return

    def __repr__(self):
        """Simple representation of the stacks."""
        out = StringIO()
        for i in (1, 2, 3):
            start = self._getBottomIndex(i)
            top = self._getTopIndex(i)
            l = self._data[start:top + 1]  # end of splice is exclusive
            out.write("{} -> {}\n".format(i, repr(l)))
        return out.getvalue()[:-1]  # without the final newline


