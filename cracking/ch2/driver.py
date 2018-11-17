from linkedlists import *

l0 = l1 = l2 = l3 = l4 = l5 = None
def reset():
    global l0, l1, l2, l3, l4, l5
    l0 = None
    l1 = makeLinkedList([1])
    l2 = makeLinkedList([1, 2, 3, 4, 5])
    l3 = makeLinkedList(['a', 'b', 'c', 'd', 'e'])
    l4 = makeLinkedList([1, 2, 3, 1, 2, 4])
    l5 = makeLinkedList([-1, -5, 6, 1, 2, 0])

if __name__ == '__main__':
    reset()
    # q1 remove duplicates in a linked list
    print """\n======= Q1 =======\n"""
    for ll in (l0, l1, l2, l3, l4):
        print "Removing dups from: \t", repr(ll)
        print "Dups removed: \t\t", repr(removeDups(ll))

    reset()
    # q2 return kth to last element of a singly linked list
    print """\n======= Q2 =======\n"""
    print "sample: ", repr(l3)
    for i in range(6):
        print "{} from last: {}".format(i, fromLast(l3, i))

    reset()
    # q3 delete "middle" node
    print """\n======= Q3 =======\n"""
    for ll in (l0, l1, l2, l3, l4):
        print "Removing middle node from: \t", repr(ll)
        print "removeMiddleNode(): \t\t", repr(removeMiddleNode(ll))
        print "After removal: \t\t\t", repr(ll)
        print "\n"

    reset()
    # q4 partition around x
    print """\n======= Q4 =======\n"""
    for ll in (l0, l1, l2, l4, l5):
        for i in (2, 3):
            print "Before: \t\t", repr(ll)
            print "Partitioning around {}...".format(i)
            partitionAround(ll, i)
            print "Done: \t\t\t", repr(ll)
            print '\n'
        print "\n"
