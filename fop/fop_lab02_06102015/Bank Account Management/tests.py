__author__ = 'cosmin'

'''
Module to test all the functions from the module commands.py.
The name of the test functions are according to the function they test.
That is, if a function is called myFunction(), then the test function will be named
testMyFunction()

It also checks for raise Exception, edge cases and so on.
'''

from exceptions import CommandError, InvalidParameters
from commands import *

def testRepresentsInt():
    assert representsInt(100) == True
    assert not representsInt("Python is nice.")
    assert representsInt(0) == True
    assert representsInt(-100) == True
    assert not representsInt("Python cannot convert string to int.")

def testGetAddTransaction():
    assert getAddTransaction(["add", "10,in,cool", "description"]) == (datetime.datetime.now().day, 10, "in", "cool description")
    assert getAddTransaction(["add", "100,out,cosmin", "rusu"]) == (datetime.datetime.now().day, 100,"out","cosmin rusu")
    try:
        getAddTransaction(["add"])
        assert False
    except CommandError:
        pass
    try:
        getAddTransaction(["add", "15,inout,salary"])
        assert False
    except InvalidParameters:
        pass
    try:
        getAddTransaction(["add", "in,in,salary"])
        assert False
    except InvalidParameters:
        pass

def testGetInsertTransaction():
    assert getInsertTransaction(["insert", "12,10,in,desc", "ription"]) == (12, 10, "in", "desc ription")
    assert getInsertTransaction(["insert", "13,100,in,desc", "ription"]) == (13, 100, "in", "desc ription")
    assert getInsertTransaction(["insert", "1,5,out,desc", "ription"]) == (1, 5, "out", "desc ription")
    try:
        getInsertTransaction(["insert"])
        assert False
    except CommandError:
        pass
    try:
        getInsertTransaction(["insert", "data,12,description"])
        assert False
    except InvalidParameters:
        pass
    try:
        getInsertTransaction(["insert", "-1,12,in,description"])
        assert False
    except InvalidParameters:
        pass
    try:
        getInsertTransaction(["insert", "1,in,out,description"])
        assert False
    except InvalidParameters:
        pass
    try:
        getInsertTransaction(["insert", "-1,-12,in,description"])
        assert False
    except InvalidParameters:
        pass
    try:
        getInsertTransaction(["insert", "1,12,input,description"])
        assert False
    except InvalidParameters:
        pass

def testGetRemoveTransactionDay():
    assert getRemoveTransactionDay(["remove", "1"]) == 1
    assert getRemoveTransactionDay(["remove", "128"]) == 128
    try:
        getRemoveTransactionDay(["remove", "amount"])
        assert False
    except InvalidParameters:
        pass
    try:
        getRemoveTransactionDay(["remove", "-1"])
        assert False
    except InvalidParameters:
        pass

def testGetRemoveTransactionInterval():
    assert getRemoveTransactionInterval(["remove", "from", "3", "to", "4"]) == (3, 4)
    assert getRemoveTransactionInterval(["remove", "from", "5", "to", "15"]) == (5, 15)
    try:
        getRemoveTransactionInterval(["remove", "to", "5", "to", "15"])
        assert False
    except CommandError:
        pass
    try:
        getRemoveTransactionInterval(["remove", "from", "-5", "to", "15"])
        assert False
    except InvalidParameters:
        pass
    try:
        getRemoveTransactionInterval(["remove", "from", "5", "to", "1"])
        assert False
    except InvalidParameters:
        pass

def testGetRemoveTypeTransaction():
    assert getRemoveTypeTransaction(["remove", "in"]) == "in"
    assert getRemoveTypeTransaction(["remove", "out"]) == "out"
    try:
        getRemoveTypeTransaction(["remove", "inout"])
        assert False
    except InvalidParameters:
        pass

def testReplaceTransaction():
    assert getReplaceTransaction(["replace", "12,in,description", "with", "200"]) == (12, "in", 200, "description")
    assert getReplaceTransaction(["replace", "13,out,description", "with", "700"]) == (13, "out", 700, "description")
    try:
        getReplaceTransaction(["replace", "13,out,description", "with"])
        assert False
    except CommandError:
        pass
    try:
        getReplaceTransaction(["replace", "13,out,description", "to", "amount"])
        assert False
    except CommandError:
        pass
    try:
        getReplaceTransaction(["replace", "13,out,description", "with", "newAmount"])
        assert False
    except InvalidParameters:
        pass
    try:
        getReplaceTransaction(["replace", "13,out,description", "with", "-700"])
        assert False
    except InvalidParameters:
        pass
    try:
        getReplaceTransaction(["replace", "13,description", "with", "700"])
        assert False
    except CommandError:
        pass
    try:
        getReplaceTransaction(["replace", "day,out,description", "with", "700"])
        assert False
    except InvalidParameters:
        pass
    try:
        getReplaceTransaction(["replace", "-13,in,description", "with", "700"])
        assert False
    except InvalidParameters:
        pass
    try:
        getReplaceTransaction(["replace", "13,inout,description", "with", "700"])
        assert False
    except InvalidParameters:
        pass

def testGetProperties():
    assert getProperties(["greater", "than", "100"]) == ["greater", 100]
    assert getProperties(["greater", "than", "10"]) == ["greater", 10]
    assert getProperties(["less", "than", "100"]) == ["less", 100]
    assert getProperties(["less", "than", "100", "before", "25"]) == ["less", 100, 25]
    try:
        getProperties(["less", "tham", "100", "before", "25""greater tham 100"])
        assert False
    except CommandError:
        pass
    try:
        getProperties(["less", "than", "100", "befoe", "25"])
        assert False
    except CommandError:
        pass
    try:
        getProperties(["less", "than"])
        assert False
    except CommandError:
        pass
    try:
        getProperties(["less", "than", "100", "25"])
        assert False
    except CommandError:
        pass
    try:
        getProperties(["less", "than", "-1", "before", "25"])
        assert False
    except InvalidParameters:
        pass
    try:
        getProperties(["less", "than", "100", "before", "-25"])
        assert False
    except InvalidParameters:
        pass

def testAllArguments():
    assert getAllArguments(["all", "in"]) == "in"
    assert getAllArguments(["all", "out"]) == "out"
    try:
        getAllArguments(["all", "100"])
        assert False
    except InvalidParameters:
        pass
    try:
        getAllArguments(["all"])
        assert False
    except CommandError:
        pass

def testGetBalanceArguments():
    assert getBalanceArguments(["balance", "100"]) == 100
    assert getBalanceArguments(["balance", "10000"]) == 10000
    try:
        getBalanceArguments(["balance"])
        assert False
    except CommandError:
        pass
    try:
        getBalanceArguments(["balance", "day"])
        assert False
    except InvalidParameters:
        pass
    try:
        getBalanceArguments(["balance", "-1"])
        assert False
    except InvalidParameters:
        pass

def testGetSumArgument():
    assert getSumArgument(["sum", "in"]) == "in"
    assert getSumArgument(["sum", "out"]) == "out"
    try:
        getSumArgument(["sum"])
        assert False
    except CommandError:
        pass
    try:
        getSumArgument(["sum", "100"])
        assert False
    except InvalidParameters:
        pass

def testGetMaxArguments():
    assert getMaxArguments(["max", "in", "day"]) == "in"
    assert getMaxArguments(["max", "out", "day"]) == "out"
    try:
        getMaxArguments(["max"])
        assert False
    except CommandError:
        pass
    try:
        getMaxArguments(["max", "inout", "day"])
        assert False
    except InvalidParameters:
        pass
    try:
        getMaxArguments(["max", "in", "150"])
        assert False
    except CommandError:
        pass

def testGetSortArguments():
    assert getSortArguments(["asc", "sort", "day"]) == ("asc", "day")
    assert getSortArguments(["desc", "sort", "in"]) == ("desc", "in")
    assert getSortArguments(["desc", "sort", "out"]) == ("desc", "out")
    try:
        getSortArguments(["asc"])
        assert False
    except CommandError:
        pass
    try:
        getSortArguments(["asc", "sorteaza", "day"])
        assert False
    except CommandError:
        pass
    try:
        getSortArguments(["desc", "sort", "150"])
        assert False
    except CommandError:
        pass

def testUndoRedo():
    transactionPack = [[(1, 1, 'in', 'a'), (2, 2, 'out', 'b'), (3, 3, 'in', 'c'), (4, 4, 'out', 'd')], [[], [(1, 1, 'in', 'a')], [(1, 1, 'in', 'a'), (2, 2, 'out', 'b')], [(1, 1, 'in', 'a'), (2, 2, 'out', 'b'), (3, 3, 'in', 'c')]]]
    transactionPack = undo(transactionPack)
    assert transactionPack == [[(1, 1, 'in', 'a'), (2, 2, 'out', 'b'), (3, 3, 'in', 'c')], [ [], [(1, 1, 'in', 'a')], [(1, 1, 'in', 'a'), (2, 2, 'out', 'b')] ], [(1, 1, 'in', 'a'), (2, 2, 'out', 'b'), (3, 3, 'in', 'c'), (4, 4, 'out', 'd')]]
    transactionPack = undo(transactionPack)
    assert transactionPack == [[(1, 1, 'in', 'a'), (2, 2, 'out', 'b')], [[], [(1, 1, 'in', 'a')]], [(1, 1, 'in', 'a'), (2, 2, 'out', 'b'), (3, 3, 'in', 'c')]]
    transactionPack = redo(transactionPack)
    assert transactionPack == [[(1, 1, 'in', 'a'), (2, 2, 'out', 'b'), (3, 3, 'in', 'c')], [ [], [(1, 1, 'in', 'a')], [(1, 1, 'in', 'a'), (2, 2, 'out', 'b')] ]]

def runTests():
    testRepresentsInt()
    testGetAddTransaction()
    testGetInsertTransaction()
    testGetRemoveTransactionDay()
    testGetRemoveTypeTransaction()
    testGetRemoveTransactionInterval()
    testReplaceTransaction()
    testGetProperties()
    testAllArguments()
    testGetBalanceArguments()
    testGetSumArgument()
    testGetMaxArguments()
    testGetSortArguments()
    testUndoRedo()