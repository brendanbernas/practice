from StringIO import StringIO

class Node:
    """
    A simple implementation of a singly linked list node
    """
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        """
        Returns a string representation from this node to end
        For simplicity, if we try to print more than 99 nodes at once, we raise an exception. 
        Helpful when we accidentally create an infinite linked list.
        """
        out = StringIO()
        out.write('[')
        node = self
        counter = 0
        while node:
            out.write(repr(node.val))
            node = node.next
            if node:
                out.write(' -> ')
            if counter > 99:
                print 
                raise ValueError('Linked list imploded. "Broken snapshot: {}"'.format(out.getvalue()))
            counter += 1
        out.write(']')
        return out.getvalue()

def makeLinkedList(li):
    """
    Helper function to create a linked list using a list object
    """
    prev = None
    first = None
    for item in li:
        node = Node(item)
        if prev:
            # set previous node to this node
            prev.next = node
        else:
            # no previous, meaning this if the first node
            first = node
        prev = node # for next iter
    return first
        

# 2.1 remove duplicates from an unsorted linked list
def removeDups(node):
    first = prev = curr = node  # no possible dups until second iteration, this is fine
    found = set()
    while curr:
        if curr.val in found:
            # set prev to next, skipping this node
            prev.next = curr.next
            # don't iterate previous
        else:
            # add to set, iterate previous
            found.add(curr.val)
            prev = curr
        
        curr = curr.next
    return first

# 2.2 return kth to last node
# ex LinkedList -> ['1', '2', '3', '4'], 1 (1st) from last is '3'. This assumes 0th is the last node
def fromLast(node, num):
    nodes = []
    curr = node
    while curr:
        # fill a list with the nodes
        nodes.append(curr)
        curr = curr.next
    if len(nodes) <= num:
        return None
    return nodes[len(nodes) - 1 - num]

# 2.3 delete "middle" node
def removeMiddleNode(node):
    first = node
    second = third = None
    if first:
        second = first.next
    if second:
        third = second.next
    if third:
        first.next = third
        return True
    return False

# 2.4 partition list around value x
def partitionAround(node, x):
    if not node:
        return None
    
    leftFirst = leftEnd = rightFirst = rightEnd = None
    curr = node
    while curr:
        if curr.val >= x:
            # populate right side
            if not rightFirst:
                rightFirst = rightEnd = curr
            else:
                rightEnd.next = curr
                rightEnd = curr
        else:
            # populate left side
            if not leftFirst:
                leftFirst = leftEnd = curr
            else:
                leftEnd.next = curr
                leftEnd = curr

        curr = curr.next

    if not leftFirst:
        return rightFirst
    
    leftEnd.next = rightFirst
    if rightEnd:
        # end our linked list
        rightEnd.next = None
    return leftFirst