# Driver to explain/run solutions for chapter 3 questions

# Q1: Describe how you could use a single array to implement three stacks


# process...
# first, are our stacks going to have a set cap, or do we want them to be dynamic?
# let's say we have a cap, and when initializing our 'ThreeStack' object, we supply
# the cap size of a single Stack.

# get the cap size, create an array triple that size
# we'll have three variables to keep track of the 'top' of each stack
#   pushing to stack will increment this variable
#   popping from the stack will decrement this variable
#   must be careful we do not push too far (into another stack or index out of upper bounds)
#       or be pop too far (also into another stack or index out of lower bounds)
#       we can use math for this one.

from three_stacks import ThreeStacks

q1 = ThreeStacks(3)

# Q2: Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

from stack_min import StackMin

q2 = StackMin()
q2.push(3)
q2.push(2)
q2.push(3)
q2.push(1)

# Q3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack)

from set_of_stacks import SetOfStacks

# Start with 15, 3 stacks of fix
q3 = SetOfStacks()  # starts with 5 as max size
for i in range(15):
    q3.push(`i`)

# Q4 Implement a MyQueue class which implements a queue using two stacks.

