__author__ = 'cosmin'

from exceptions import InvalidParameters, SyntaxError
from tests import representsInt

def getProperties(command):
    if len(command) < 3:
        raise SyntaxError("Filter command - Syntax error!")
    if len(command) == 4:
        raise SyntaxError("Filter command - Syntax error!")
    if command[1] != 'than':
        raise SyntaxError("Filter command - Syntax error!")
    if len(command) > 3 and command[3] != 'before':
        raise SyntaxError("Filter command - Syntax error!")
    if not representsInt(command[2]):
        raise ValueError("Filter command - amount is not an integer!")
    if int(command[2]) <= 0:
        raise ValueError("Filter command - amount should be strictly positive!")
    if len(command) > 3 and not representsInt(command[4]):
        raise ValueError("Filter command - day is not an integer!")
    if len(command) > 3 and int(command[4]) <= 0:
        raise ValueError("Filter command - day should be strictly positive!")
    arguments = [command[0], int(command[2])]
    if len(command) > 3:
        arguments.append(int(command[4]))
    return arguments

def filterPropertyTransactions(command, transactionList):
    try:
        arguments = getProperties(command)
        if arguments[0] == 'greater':
            if len(arguments) == 2:
                return [transaction for transaction in transactionList if transaction[1] >= arguments[1]]
            else:
                return [transaction for transaction in transactionList if transaction[1] >= arguments[1] and transaction[0] <= arguments[2]]
        else:
           if len(arguments) == 2:
                return [transaction for transaction in transactionList if transaction[1] <= arguments[1]]
           else:
                return [transaction for transaction in transactionList if transaction[1] <= arguments[1] and transaction[0] <= arguments[2]]
    except SyntaxError as se:
        print(str(se))
    except ValueError as ve:
        print(str(ve))
    return None

def getAllArguments(command):
    if len(command) < 2:
        raise SyntaxError("All filter - syntax error!")
    if command[1] != "in" and command[1] != 'out':
        raise InvalidParameters("All filter - the only known types are in/out")
    return command[1]

def filterAllTransactions(command, transactionList):
    try:
        arg = getAllArguments(command)
        return [transaction for transaction in transactionList if transaction[2] == arg]
    except SyntaxError as se:
        print(str(se))
    except ValueError as ve:
        print(str(ve))
    return None

def getBalanceArguments(command):
    if len(command) < 2:
        raise SyntaxError("Balance - syntax error!")
    if not representsInt(command[1]):
        raise ValueError("Balance - day should be integer!")
    if int(command[1]) <= 0:
        raise ValueError("Balance - day should be positive!")
    return int(command[1])

def computeBalance(command, transactionList):
    try:
        arg = getBalanceArguments(command)
        sum = 0
        for transaction in transactionList:
            if transaction[0] == arg:
                if transaction[2] == 'in':
                    sum += transaction[1]
                else:
                    sum -= transaction[1]
        return sum
    except SyntaxError as se:
        print(str(se))
    except ValueError as ve:
        print(str(ve))
    return None



