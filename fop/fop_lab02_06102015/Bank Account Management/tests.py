__author__ = 'cosmin'

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
    except ValueError:
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
    except ValueError:
        pass
    try:
        getInsertTransaction(["insert", "1,in,out,description"])
        assert False
    except ValueError:
        pass
    try:
        getInsertTransaction(["insert", "-1,-12,in,description"])
        assert False
    except ValueError:
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
    except ValueError:
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
    except ValueError:
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
    except ValueError:
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
    except ValueError:
        pass
    try:
        getReplaceTransaction(["replace", "13,out,description", "with", "-700"])
        assert False
    except ValueError:
        pass
    try:
        getReplaceTransaction(["replace", "13,description", "with", "700"])
        assert False
    except CommandError:
        pass
    try:
        getReplaceTransaction(["replace", "day,out,description", "with", "700"])
        assert False
    except ValueError:
        pass
    try:
        getReplaceTransaction(["replace", "-13,in,description", "with", "700"])
        assert False
    except ValueError:
        pass
    try:
        getReplaceTransaction(["replace", "13,inout,description", "with", "700"])
        assert False
    except ValueError:
        pass

def runTests():
    testRepresentsInt()
    testGetAddTransaction()
    testGetInsertTransaction()
    testGetRemoveTransactionDay()
    testGetRemoveTypeTransaction()
    testGetRemoveTransactionInterval()
    testReplaceTransaction()