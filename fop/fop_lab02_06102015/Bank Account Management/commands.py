__author__ = 'cosmin'

from exceptions import InvalidParameters, CommandError
import datetime

def representsInt(s):
    '''
    Function to return True if the :param s can be converted to int

    :param s: the string that the user has given
    :rtype : boolean
    :return: True if string s is an integer
             False is string s is not an integer
    '''
    try:
        int(s)
        return True
    except ValueError:
        return

def getAddTransaction(command):
    '''
    A function to handle the Add Transaction Feature

    :param command: the command the user has inputted
    :return a tuple (day, amount, in/out, description) which describes
                the transaction the user wants to add
            or None if there is a command syntax error
    '''
    if len(command) < 2:
        raise CommandError("Add command - Syntax Error!")
    argsList = command[1].split(',')
    if len(argsList) < 3:
        raise InvalidParameters("Add command - Not enough parameters!")
    if not representsInt(argsList[0]):
        raise ValueError("Add command - The amount of money not an integer!")
    if int(argsList[0]) <= 0:
        raise ValueError("Add command - The amount of money should be strictly positive!")
    if argsList[1].lower() not in ["in", "out"]:
        raise InvalidParameters("Add command - The only known types are in and out!")
    description = ','.join(argsList[2:])
    if len(command) > 2:
        description = description + ' ' + ' '.join(command[2:])
    transaction = (datetime.datetime.now().day, int(argsList[0]), argsList[1], description)
    return transaction

def addTransaction(command, transactionList):
    '''
    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    newTransaction = None
    try:
        newTransaction = getAddTransaction(command)
    except ValueError as ve:
        print(str(ve))
    except CommandError as se:
        print(str(se))
    except InvalidParameters as ie:
        print(str(ie))
    if newTransaction is not None:
        transactionList.append(newTransaction)
    return transactionList

def getInsertTransaction(command):
    '''
    A function to handle the Insert Transaction Feature

    :param command: the command the user has inputted
    :return a tuple (day, amount, in/out, description) which describes
                the transaction the user wants to insert
            or None if there is a command syntax error
    '''
    if len(command) < 2:
        raise CommandError("Insert Command - Syntax Error!")
    argsList = command[1].split(',')
    if len(argsList) < 4:
        raise InvalidParameters("Insert Command - Not enough parameters!")
    if not representsInt(argsList[0]):
        raise ValueError("Insert Command - Day not an integer!")
    if int(argsList[0]) <= 0:
        raise ValueError("Insert Command - Day should be strictly positive!")
    if not representsInt(argsList[1]):
        raise ValueError("Insert Command - Amount not an integer!")
    if int(argsList[1]) <= 0:
        raise ValueError("Insert Command - Amount cannot be negative or nul!")
    if argsList[2].lower() not in ["in", "out"]:
        raise InvalidParameters("Insert Command - The only known transaction types are in and out")
    description = ','.join(argsList[3:])
    if len(command) > 2:
        description = description + ' ' + ' '.join(command[2:])
    transaction = (int(argsList[0]), int(argsList[1]), argsList[2], description)
    return transaction


def insertTransaction(command, transactionList):
    '''
    Function to update the list with the correct new insert transaction

    :param command: a list representing the command the user wants to make, which is the string split by spaces
    :param transactionList: a list of tuples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    newTransaction = None
    try:
        newTransaction = getInsertTransaction(command)
    except ValueError as ve:
        print(str(ve))
    except CommandError as se:
        print(str(se))
    except InvalidParameters as ie:
        print(str(ie))
    if newTransaction is not None:
        transactionList.append(newTransaction)
    return transactionList

def getRemoveTransactionDay(command):
    '''
    Function to parse the remove command and to return the transaction day that needs to be removed
    :param command:
    :return: an integer - the date parsed from the command
    '''
    if representsInt(command[1]) == False:
        raise ValueError("Remove Command - Day not an integer!")
    if int(command[1]) <= 0:
        raise InvalidParameters("Remove Command - Date should be strictly positive")
    return int(command[1])

def removeTransactionDay(command, transactionList):
    '''
    Function to remove all the transaction from a specific day

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of tuples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    day = None
    try:
        day = getRemoveTransactionDay(command)
    except ValueError as ve:
        print(str(ve))
    except CommandError as se:
        print(str(se))
    except InvalidParameters as ie:
        print(str(ie))
    return [transaction for transaction in transactionList if transaction[0] != day]

def getRemoveTransactionInterval(command):
    '''
    A function to handle the Remove Interval Transaction

    :param command: the command the user has inputted
    :return a tuple (startDay, endDay) which describes
                the date interval that the user wants to remoev
            or None if there is a command syntax error
    :raise CommandError, ValueError, SyntaxError
    '''
    if command[1] != 'from' or command[3] != 'to':
        raise CommandError("Remove command - Syntax Error!")
    if representsInt(command[2]) == False or representsInt(command[4]) == False:
        raise ValueError("Remove command - Dates should be integers!")
    if int(command[2]) <= 0:
        raise ValueError("Remove command - Days should be strictly!")
    startDate = int(command[2])
    endDate = int(command[4])
    if startDate > endDate:
        raise InvalidParameters("Remove command - Dates do not form an interval!")
    return (startDate, endDate)

def removeTransactionInterval(command, transactionList):
    '''
    Function to remove all the transaction from a specific interval of days

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        (startDate, endDate) = getRemoveTransactionInterval(command)
        return [transaction for transaction in transactionList if not startDate <= transaction[0] <= endDate]
    except CommandError as ce:
        print(str(ce))
    except ValueError as ve:
        print(str(ve))
    except InvalidParameters as ip:
        print(str(ip))
    return transactionList

def getRemoveTypeTransaction(command):
    '''
    Function to get the parameter of the Remove Type(in/out) transaction
    :param command:
    :return:
    '''
    if command[1] != 'in' and command[1] != 'out':
        raise ValueError("Remove command - The only known types of transactions are in and out!")
    return command[1]

def removeTypeTransaction(command, transactionList):
    '''
    Function to remove all the transaction with the type given by user (in / out)

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    arg = None
    try:
        arg = getRemoveTypeTransaction(command)
        return [transaction for transaction in transactionList if transaction[2] != arg]
    except ValueError as ve:
        print(str(ve))
    return None

def removeTransaction(command, transactionList):
    '''
    Function to determine which remove function to be called, because there are 3 typed of remove functions:
        remove X – removes all the transactions from day X")
        remove from X to Y – removes all the transactions from day X until day Y")
        remove in/out – removes all the in/out transactions from the current month")

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    if len(command) <= 1:
        print("not enough parameters")
        return transactionList
    elif len(command) == 2:
        if command[1] in ["in", "out"]:
            return removeTypeTransaction(command, transactionList)
        else:
            return removeTransactionDay(command, transactionList)
    elif len(command) == 5:
        return removeTransactionInterval(command, transactionList)
    else:
        print('syntax error')
        return transactionList

def getReplaceTransaction(command):
    '''
    A function to handle the Replace Transaction Feature

    :param command: the command the user has inputted
                the transaction the user wants to insert
    '''
    if len(command) < 4:
        raise CommandError("Replace command - Syntax error!")
    if command[-2] != 'with':
        raise CommandError("Replace command - Syntax error!")
    if representsInt(command[-1]) == False:
        raise ValueError("Replace command - Amount not an integer!")
    if int(command[-1]) <= 0:
        raise ValueError('Replace command - Amount cannot be negative or null!')
    argsList = command[1].split(',')
    if len(argsList) < 3:
        raise CommandError("Replace command - Not enough parameters!")
    if representsInt(argsList[0]) == False:
        raise ValueError("Replace command - Date not an integer!")
    if int(argsList[0]) <= 0:
        raise ValueError("Replace command - Date should be strictly positive!")
    if argsList[1] not in ['in', 'out']:
        raise ValueError('Replace command - Transaction type unknown, should be only in or out')
    newAmount = int(command[-1])
    day = int(argsList[0])
    description = ','.join(argsList[2:])
    if len(command) > 4:
        description = description + ' ' + ' '.join(command[2:-2])
    return (day, argsList[1], newAmount, description)

def replaceTransaction(command, transactionList):
    '''
    Function to replace a transaction's amount of money.

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    (day, type, newAmount, description) = (None, None, None, None)
    try:
        (day, type, newAmount, description) = getReplaceTransaction(command)
    except ValueError as ve:
        print(str(ve))
    except CommandError as se:
        print(str(se))
    except InvalidParameters as ie:
        print(str(ie))
    for i in range(len(transactionList)):
        if transactionList[i][0] == day and transactionList[i][2] == type and transactionList[i][3] == description:
            transactionList[i] = (transactionList[i][0], newAmount, transactionList[i][2], transactionList[i][3])
    return transactionList


def getProperties(command):
    '''
    Function to return a list containing the properties of the filter query
    :param command: a list containing the user command, split by whitespaces
    :return:  another list containing the arguments of the filter command which can be of two types:
        greater/less than X - all transactions greater/less than X (given amount of money)
        greater/less than X before Y - all transactions greater/less than X (given amount of money) before given day(Y)
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    if len(command) < 3:
        raise CommandError("Filter command - Syntax error!")
    if len(command) == 4:
        raise CommandError("Filter command - Syntax error!")
    if command[1] != 'than':
        raise CommandError("Filter command - Syntax error!")
    if len(command) > 3 and command[3] != 'before':
        raise CommandError("Filter command - Syntax error!")
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
    '''
    Function to return a new list which contains the filtered list by the 'mask' given by the user.
    :param command:
    :param transactionList:
    :return: another list - filteredList
    '''
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
    except CommandError as se:
        print(str(se))
    except ValueError as ve:
        print(str(ve))
    return None

def getAllArguments(command):
    '''
    Function to get the arguments of All command
    :param command: a list containing the whitespace-split command from the user
    :return: either 'in' or 'out' parsed from what the user inserted
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    if len(command) < 2:
        raise CommandError("All filter - syntax error!")
    if command[1] != "in" and command[1] != 'out':
        raise InvalidParameters("All filter - the only known types are in/out")
    return command[1]

def filterAllTransactions(command, transactionList):
    '''
    Function to return the filtered transaction, that is, all the 'in' tranasction or the 'out' transactions
    :param command:
    :param transactionList:
    :return: another list which is sublist of transactionList or None if there are exceptions
    '''
    try:
        arg = getAllArguments(command)
        return [transaction for transaction in transactionList if transaction[2] == arg]
    except CommandError as se:
        print(str(se))
    except ValueError as ve:
        print(str(ve))
    return None

def getBalanceArguments(command):
    '''
    Function to get the arguments of Balance command
    :param command: a list containing the whitespace-split command from the user
    :return: an integer representing the day when the use wants to know it's balance
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    if len(command) < 2:
        raise CommandError("Balance - syntax error!")
    if not representsInt(command[1]):
        raise ValueError("Balance - day should be integer!")
    if int(command[1]) <= 0:
        raise ValueError("Balance - day should be positive!")
    return int(command[1])

def computeBalance(command, transactionList):
    '''
    Function to compute the balance of the given day.
    :param command:
    :param transactionList:
    :return:an integer representing the balance up the the given day
    '''
    try:
        arg = getBalanceArguments(command)
        sum = 0
        for transaction in transactionList:
            if transaction[0] <= arg:
                if transaction[2] == 'in':
                    sum += transaction[1]
                else:
                    sum -= transaction[1]
        return sum
    except CommandError as se:
        return str(se)
    except ValueError as ve:
        return str(ve)

def getSumArgument(command):
    '''
    Function to get the arguments of Sum command
    :param command: a list containing the whitespace-split command from the user
    :return: an integer representing the sum of all the 'in' transaction or 'out' transaction.
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    if len(command) < 2:
        raise CommandError("Sum command - Syntax error!")
    if command[1] != 'in' and command[1] != 'out':
        raise ValueError("Sum command - Unknown transaction type!")
    return command[1]

def getSum(command, transactionList):
    '''
    Function to return the sum for the given arguments
    :param command: the list containing the whitespace-split command from the user
    :param transactionList:
    :return: the sum of the filtere transactions
    '''
    try:
        arg = getSumArgument(command)
        return sum([transaction[1] for transaction in transactionList if transaction[2] == arg])
    except CommandError as se:
        return str(se)
    except ValueError as ve:
        return str(ve)

def getMaxArguments(command):
    '''
    Function to get the arguments of Max command
    :param command: a list containing the whitespace-split command from the user
    :return: an string from the set {"in", "out"} which is the argumet of the max command
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    if len(command) < 3:
        raise CommandError("Max command - Syntax error!")
    if command[1] != 'in' and command[1] != 'out':
        raise ValueError("Max command - Unknown type of transaction")
    if command[2] != 'day':
        raise CommandError("Max command - Syntax error!")
    return command[1]

def getMax(command, transactionList):
    '''
    Function the compute the Max command or to raise the exception whenever the command is invalid.
    :param command:
    :param transactionList:
    :return: am integer representing the day with the maximum amount in an out transaction
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    try:
        args = getMaxArguments(command)
        maximum = -1
        day = 0
        print(args)
        for transaction in transactionList:
            if transaction[2] == args and maximum < transaction[1]:
                maximum = transaction[1]
                day = transaction[0]
        if day == 0:
            return "List is empty!"
        return day
    except CommandError as se:
        return str(se)
    except ValueError as ve:
        return str(ve)

def getSortArguments(command):
    '''
    Function to get the arguments of Sort command
    :param command: a list containing the whitespace-split command from the user
    :return: a tuple ('asc'/'desc', 'day'/'in'/'out') representing the arguments the the sort function
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    if len(command) < 3:
        raise CommandError("Sort command - Syntax Error!")
    if command[1] != 'sort':
        raise CommandError("Sort command - Syntax Error!")
    if command[2] != 'day' and command[2] != 'in' and command[2] != 'out':
        raise CommandError("Sort command - Syntax Error!")
    return (command[0], command[2])

def sortTransactions(command, transactionList):
    '''
    Function to return the sorted transaction list by the comparator given by the user.
    :param command:
    :param transactionList:
    :return: another list containing the sorted list
    '''
    try:
        args = getSortArguments(command)
        if args[1] == 'day':
            if args[0] == 'asc':
                return sorted(transactionList, key = lambda transaction : transaction[1])
            elif args[0] == 'desc':
                return sorted(transactionList, key = lambda transaction : transaction[1], reverse=True)
        else:
            if args[0] == 'asc':
                return sorted([transaction for transaction in transactionList if transaction[2] == args[1]], key = lambda transaction : transaction[1])
            else:
                return sorted([transaction for transaction in transactionList if transaction[2] == args[1]], key = lambda transaction : transaction[1], reverse=True)
    except CommandError as se:
        return str(se)
    except ValueError as ve:
        return str(ve)