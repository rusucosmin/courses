def substitute(l, i, v):
    if l == []:
        return []
    elif i == 0:
        return [ v ] + substitute(l[1:], i - 1, v)
    else:
        return [ l[0] ] + substitute(l[1:], i - 1, v)

def isIn(l, v):
    if l == []:
        return False
    elif l[0] == v:
        return True
    else:
        return isIn(l[1:], v)

def difference(l1, l2):
    if l1 == []:
        return []
    elif not isIn(l2, l1[0]):
        return [ l1[0] ] + difference(l1[1:], l2)
    else:
        return difference(l1[1:], l2)

#unit tests for substitute
assert substitute([1, 2, 3], 1, 5) == [1, 5, 3]
assert substitute([1, 2, 3], 100, 0) == [1, 2, 3]
assert substitute([1, 2, 3], 0, -1) == [-1, 2, 3]

#unit tests for difference
assert difference([1, 2, 3], [1, 2]) == [3]
assert difference([1, 2, 4], [1, 2, 4]) == []
assert difference([1, 2, 3], [4, 5, 6]) == [1, 2, 3]
