from random import randint, choice

from model.book import Book

'''
Module to implement the sorting and the filtering fucntionality.
Each module can be independently used on later projects
'''

def gnomeSort(iterable, cmpFunction=None, reverse=False):
    '''
    My implementation for Gnome sort algorithm
    :param iterable: data structure that will be sorted
    :param cmpFunction:Function that will be used for comparing elements. < used if None
    :param reverse:S ort in reversed order
    :return: the iterable data structure, sorted by the cmpFunction
    '''
    if iterable == None:
        return None
    if reverse == True:
        reverse = -1
    else:
        reverse = 1
    pos=1
    while pos < len(iterable):
        if cmpFunction == None:
            if reverse * (iterable[pos] - iterable[pos - 1]) >= 0:
                pos += 1
            else:
                iterable[pos], iterable[pos - 1] = iterable[pos - 1], iterable[pos]
                if pos > 1:
                    pos -= 1
        else:
            if reverse * cmpFunction(iterable[pos], iterable[pos - 1]) >= 0:
                pos += 1
            else:
                iterable[pos], iterable[pos - 1] = iterable[pos - 1], iterable[pos]
                if pos > 1:
                    pos -= 1
    return iterable


def myFilter(iterable, filterFct):
    '''
    Filter function
    :param iterable: iterable list to be filtered
    :param filterFct: function to check if an element should be filtere or not
    :return:
    '''
    return [x for x in iterable if filterFct(x)]

def isSorted(iterable, cmpFunction=None, reverse=False):
    '''
    Function to check if the list was sorted or not
    :param iterable: data structure that has to be checked
    :param cmpFunction:Function that will be used for comparing elements. < used if None
    :param reverse: Reversed order
    :return: True if the list is sorted or False otherwise
    '''
    n = len(iterable)
    if reverse == True:
        reverse = -1
    else:
        reverse = 1
    for i in range(n - 1):
        if cmpFunction == None:
            if reverse * (iterable[i] - iterable[i + 1]) > 0:
                return False
        else:
            if reverse * cmpFunction(iterable[i], iterable[i + 1]) > 0:
                return False
    return True

def testSort():
    '''
    Main test function to call every subtest function
    '''
    testSpecialCases()
    testIntegerSort()
    testBooksSort()

def testSpecialCases():
    '''
    Function to test some special cases sort examples
    '''
    x = []
    assert gnomeSort(x, None, False) == []
    x = None
    assert gnomeSort(x, None, False) == None

def testBooksSort():
    '''
    Function to test the sorting of a generetic class.
    '''
    x = [
        Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen"),
        Book(1, "Dorian Gray's Portret", "Modern novel", "Oscar Wilde"),
        Book(2, "The basis of Math", "A nice book on Math for students", "Dorin Andrica")
    ]
    gnomeSort(x, booksByAuthor, False)
    assert isSorted(x, booksByAuthor, False) == True
    gnomeSort(x, booksByAuthor, True)
    assert isSorted(x, booksByAuthor, True) == True
    gnomeSort(x, booksById, False)
    assert isSorted(x, booksById, False) == True
    assert x == [
        Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen"),
        Book(1, "Dorian Gray's Portret", "Modern novel", "Oscar Wilde"),
        Book(2, "The basis of Math", "A nice book on Math for students", "Dorin Andrica")
    ] #just to be sure

def testIntegerSort():
    '''
    Function to test the sorting of random generated integer list
    '''
    for test in range(10):
        l = randint(1, 1000)
        x = [randint(1, 10000) for x in range(l)]
        gnomeSort(x, intLess, False)
        if not isSorted(x, intLess, False):
            assert False


    for test in range(10):
        l = randint(1, 100)
        x = [randint(1, 10000) for x in range(l)]
        gnomeSort(x, intGre, False)
        if not isSorted(x, intGre, False):
            assert False

#comparator functions

def booksByTitle(a, b):
    if a.getTitle() < b.getTtle():
        return -1
    elif a.getTitle() > b.getTitle():
        return 1
    else:
        return 0

def booksByAuthor(a, b):
    if a.getAuthor() < b.getAuthor():
        return -1
    elif a.getAuthor() > b.getAuthor():
        return 1
    else:
        return 0

def booksById(a, b):
    if a.getId() < b.getId():
        return -1
    elif a.getId() > b.getId():
        return 1
    else:
        return 0

def intLess(x, y):
    '''
    less comparator for two integers x, y
    :param x: the first integer
    :param y: the second one
    :return:   -1 if x < y
                1 if x > y
                0 otherwise
    '''
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

def intGre(x, y):
    '''
    greater comparator for two integers x, y
    :param x: the first integer
    :param y: the second one
    :return:   -1 if x > y
                1 if x < y
                0 otherwise
    '''
    return -intLess(x, y)