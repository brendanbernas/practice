# Page 101
# 1.1 Determine if all characters in a string is unique

# using hashmap
def isStringUnique(s):
    hashmap = {}
    for c in s:
        if c in hashmap:
            return False
        hashmap[c] = None
    return True

# not using any additional data structures
def isStringUnique2(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

# 1.2 Detemine if one string is a permutation of another

# forgot to check length of strings....
# we must count the number of occurances in each string, checking for existance is not enough
#   ex: "1222" and "1112" will return True 

def isPermutation(s1, s2):
    s1hashmap = {}
    for c in s1:
        s1hashmap[c] = None
    for c in s2:
        if c not in s1hashmap:
            return False
    return True

# 1.3 "URLify a string by converting spaces to %20"
def makeUrlFromString(strIn, size):
    from StringIO import StringIO
    out = StringIO()
    for i in range(size):
        if i < len(strIn) and strIn[i] != ' ':
            out.write(strIn[i])
        else:
            out.write('%20')
    return out.getvalue()

# 1.4 check if string can be permutated into a palindrome
def canPermutateIntoPalindrome(strIn):
    holder = {}
    for c in strIn:
        if c == ' ':
            continue
        if c.lower() not in holder:
            holder[c.lower()] = None
        else:
            del holder[c.lower()]
    if len(holder) <= 1:
        return True
    return False

# 1.5 check if a string is one or less removal, or character change away from another

# this has a run time of O(A + B)
# can actually optimize it to a run time of O(N), where N is size the smaller string

def isOneAway(strA, strB):
    if len(strA) == len(strB) == 1:  # special case
        return True
    holder = {}
    for c in strA:
        holder[c] = None
    for c in strB:
        if c in holder:
            del holder[c]
        else:
            holder[c] = None
    if len(holder) <= 1:
        return True
    return False

# the above optimized to O(N) where N is the length of the shortest string
def isOneAwayOptimized(strA, strB):
    if abs(len(strA) - len(strB)) > 1:
        return False
    # find the shorter string
    first = strA if len(strA) <= len(strB) else strB
    second = strB if len(strB) >= len(strA) else strA
    # if the length is off, we already have a difference
    foundDiff = len(strA) != len(strB)
    i = 0
    j = 0
    while i < len(first):  # loop to last index
        if first[i] != second[j]:
            if foundDiff:  # second difference found
                return False
            foundDiff = True
        i += 1
        j += 1
    return True

# 1.6 compress string
# O(N) runtime, where N is the length of the input
def compressString(s):
    from StringIO import StringIO
    # we know we cannot compress this
    if len(s) <= 2:
        return s
    counter = 1
    prevC = s[0]
    out = StringIO()
    for i in range(1, len(s) + 1):
        if i == len(s) or prevC != s[i]:
            out.write(prevC + `counter`)
            if i != len(s):
                prevC = s[i]
            counter = 1
        else:
            counter += 1
    if len(out.getvalue()) < len(s):
        return out.getvalue()
    return s

# 1.7 rotate an image image representated by an NxN matrix where each pixel is 4 bytes
# we do this here creating a new holder. runtime is O(N^2) where N is the length of matrix
# memory is O(N^2), we can probably bring this down to O(1)
def rotateMatrix1(matrix):
    size = len(matrix)
    new = [[None for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            x, y = _calculateRotatedPoint(i, j, size)
            new[x][y] = matrix[i][j]
    return new

def _calculateRotatedPoint(x, y, size):
    # x' -> y
    # y' -> abs(x - size + 1)
    return (y, abs(x - size + 1))

# 1.7 continued
# lets bring this down to O(1) memory
def rotateMatrix2(matrix):
    """
    Mutates and rotates the incoming matrix 90 degrees clockwise
    """
    size = len(matrix)
    for i in range(size/2):
        for j in range(i, size - i - 1):
            previous = matrix[i][j]
            x, y = _calculateRotatedPoint(i, j, size)
            for _ in range(4):  # change 4 places
                # get next value
                curr = matrix[x][y]
                # put previous value into next position
                matrix[x][y] = previous
                x, y = _calculateRotatedPoint(x, y, size)
                previous = curr
    return matrix
                

# some test data
a = [
    [1]
]

b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

d = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 0, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

# just a helper
def prettyMatrix(matrix):
    for x in matrix:
        print x

# 1.8 Zero Matrix. If a row ir column in a matrix has 0, make the whole row/matrix 0
def zeroMatrix(matrix):
    # could use a bitmap here
    zeroRows = {}
    zeroCols = {}
    size = len(matrix)
    # determine where 0s are first
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                # save the rows/cols with 0
                zeroRows[i] = None
                zeroCols[j] = None
    for i in range(size):
        for j in range(size):
            if i in zeroCols or j in zeroRows:
                matrix[i][j] = 0
    return matrix

# 1.9 Is String Rotation. Are s1 and s2 rotations of eachother? Ex "waterbottle" is a rotation of"erbottlewat"
# use isSubstring method, but only once. python's <str> in <str> works
def isRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) != 0:
        return s2 in s1+s1
    return False    
    
