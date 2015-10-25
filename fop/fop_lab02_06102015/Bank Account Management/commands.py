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
        raise InvalidParameters("Add command - The amount of money not an integer!")
    if int(argsList[0]) <= 0:
        raise InvalidParameters("Add command - The amount of money should be strictly positive!")
    if argsList[1].lower() not in ["in", "out"]:
        raise InvalidParameters("Add command - The only known types are in and out!")
    description = ','.join(argsList[2:])
    if len(command) > 2:
        description = description + ' ' + ' '.join(command[2:])
    transaction = (datetime.datetime.now().day, int(argsList[0]), argsList[1], description)
    return transaction

def addTransaction(command, transactionPack):
    '''
    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of tuples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        newTransaction = getAddTransaction(command)
        transactionPack[1].append(transactionPack[0][:])
        transactionPack[0].append(newTransaction)
        return (None, transactionPack)
    except CommandError as se:
        return (se, None)
    except InvalidParameters as ie:
        return (ie, None)

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
        raise InvalidParameters("Insert Command - Day not an integer!")
    if int(argsList[0]) <= 0:
        raise InvalidParameters("Insert Command - Day should be strictly positive!")
    if not representsInt(argsList[1]):
        raise InvalidParameters("Insert Command - Amount not an integer!")
    if int(argsList[1]) <= 0:
        raise InvalidParameters("Insert Command - Amount cannot be negative or nul!")
    if argsList[2].lower() not in ["in", "out"]:
        raise InvalidParameters("Insert Command - The only known transaction types are in and out")
    description = ','.join(argsList[3:])
    if len(command) > 2:
        description = description + ' ' + ' '.join(command[2:])
    transaction = (int(argsList[0]), int(argsList[1]), argsList[2], description)
    return transaction

def insertTransaction(command, transactionPack):
    '''
    Function to update the list with the correct new insert transaction

    :param command: a list representing the command the user wants to make, which is the string split by spaces
    :param transactionList: a list of tuples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        newTransaction = getInsertTransaction(command)
        transactionPack[1].append(transactionPack[0][:])
        transactionPack[0].append(newTransaction)
        return (None, transactionPack)
    except CommandError as se:
        return (se, None)
    except InvalidParameters as ie:
        return (ie, None)

def getRemoveTransactionDay(command):
    '''
    Function to parse the remove command and to return the transaction day that needs to be removed
    :param command:
    :return: an integer - the date parsed from the command
    '''
    if not representsInt(command[1]):
        raise InvalidParameters("Remove Command - Day not an integer.")
    if int(command[1]) <= 0:
        raise InvalidParameters("Remove Command - Date should be strictly positive.")
    return int(command[1])

def removeTransactionDay(command, transactionPack):
    '''
    Function to remove all the transaction from a specific day

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of tuples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        day = getRemoveTransactionDay(command)
        transactionPack[1].append(transactionPack[0][:])
        transactionPack[0] = [transaction for transaction in transactionPack[0] if transaction[0] != day]
        return (None, transactionPack)
    except CommandError as se:
        return (se, None)
    except InvalidParameters as ie:
        return (ie, None)

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
        raise InvalidParameters("Remove command - Dates should be integers!")
    if int(command[2]) <= 0:
        raise InvalidParameters("Remove command - Days should be strictly!")
    startDate = int(command[2])
    endDate = int(command[4])
    if startDate > endDate:
        raise InvalidParameters("Remove command - Dates do not form an interval!")
    return (startDate, endDate)

def removeTransactionInterval(command, transactionPack):
    '''
    Function to remove all the transaction from a specific interval of days

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        (startDate, endDate) = getRemoveTransactionInterval(command)
        transactionPack[1].append(transactionPack[0][:])
        transactionPack[0] = [transaction for transaction in transactionPack[0] if not startDate <= transaction[0] <= endDate]
        return (None, transactionPack)
    except CommandError as ce:
        return (ce, None)
    except InvalidParameters as ip:
        return (ip, None)

def getRemoveTypeTransaction(command):
    '''
    Function to get the parameter of the Remove Type(in/out) transaction
    :param command:
    :return:
    '''
    if command[1] != 'in' and command[1] != 'out':
        raise InvalidParameters("Remove command - The only known types of transactions are in and out!")
    return command[1]

def removeTypeTransaction(command, transactionPack):
    '''
    Function to remove all the transaction with the type given by user (in / out)

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionPack: a pair of a list of touples where each transaction are stored adn the history
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        arg = getRemoveTypeTransaction(command)
        transactionPack[1].append(transactionPack[0][:])
        transactionPack[0] = [transaction for transaction in transactionPack[0] if transaction[2] != arg]
        return (None, transactionPack)
    except InvalidParameters as ve:
        return (ve, None)

def chooseRemoveType(command):
    if len(command) <= 1:
        raise SyntaxError("Not enough parameters.")
    if len(command) == 2:
        if command[1] in ["in", "out"]:
            return 1 #removeTypeTransaction(command, transactionList)
        else:
            return 2 #removeTransactionDay(command, transactionList)
    if len(command) == 5:
        return 3 #removeTransactionInterval(command, transactionList)
    else:
        raise SyntaxError("Syntax error.")

def removeTransaction(command, transactionPack):
    '''
    Function to determine which remove function to be called, because there are 3 typed of remove functions:
        remove X – removes all the transactions from day X")
        remove from X to Y – removes all the transactions from day X until day Y")
        remove in/out – removes all the in/out transactions from the current month")

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of tuples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        x = chooseRemoveType(command)
        if x == 1:
            return removeTypeTransaction(command, transactionPack)
        if x == 2:
            return removeTransactionDay(command, transactionPack)
        if x == 3:
            return removeTransactionInterval(command, transactionPack)
    except SyntaxError as se:
        return (se, None)

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
    if not representsInt(command[-1]):
        raise InvalidParameters("Replace command - Amount not an integer!")
    if int(command[-1]) <= 0:
        raise InvalidParameters('Replace command - Amount cannot be negative or null!')
    argsList = command[1].split(',')
    if len(argsList) < 3:
        raise CommandError("Replace command - Not enough parameters!")
    if not representsInt(argsList[0]):
        raise InvalidParameters("Replace command - Date not an integer!")
    if int(argsList[0]) <= 0:
        raise InvalidParameters("Replace command - Date should be strictly positive!")
    if argsList[1] not in ['in', 'out']:
        raise InvalidParameters('Replace command - Transaction type unknown, should be only in or out')
    newAmount = int(command[-1])
    day = int(argsList[0])
    description = ','.join(argsList[2:])
    if len(command) > 4:
        description = description + ' ' + ' '.join(command[2:-2])
    return (day, argsList[1], newAmount, description)

def replaceTransaction(command, transactionPack):
    '''
    Function to replace a transaction's amount of money.

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of tuples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    try:
        (day, type, newAmount, description) = getReplaceTransaction(command)
        transactionPack[1].append(transactionPack[0][:])
        for i in range(len(transactionPack[0])):
            if transactionPack[0][i][0] == day and transactionPack[0][i][2] == type and transactionPack[0][i][3] == description:
                transactionPack[0][i] = (transactionPack[0][i][0], newAmount, transactionPack[0][i][2], transactionPack[0][i][3])
        return (None, transactionPack)
    except CommandError as se:
        return (se, None)
    except InvalidParameters as ie:
        return (ie, None)

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
        raise InvalidParameters("Filter command - amount is not an integer!")
    if int(command[2]) <= 0:
        raise InvalidParameters("Filter command - amount should be strictly positive!")
    if len(command) > 3 and not representsInt(command[4]):
        raise InvalidParameters("Filter command - day is not an integer!")
    if len(command) > 3 and int(command[4]) <= 0:
        raise InvalidParameters("Filter command - day should be strictly positive!")
    arguments = [command[0], int(command[2])]
    if len(command) > 3:
        arguments.append(int(command[4]))
    return arguments

def filterPropertyTransactions(command, transactionPack):
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
                return (None, [transaction for transaction in transactionPack[0] if transaction[1] >= arguments[1]])
            else:
                return (None, [transaction for transaction in transactionPack[0] if transaction[1] >= arguments[1] and transaction[0] <= arguments[2]])
        else:
           if len(arguments) == 2:
                return (None, [transaction for transaction in transactionPack[0] if transaction[1] <= arguments[1]])
           else:
                return (None, [transaction for transaction in transactionPack[0] if transaction[1] <= arguments[1] and transaction[0] <= arguments[2]])
    except CommandError as se:
        return (se, None)
    except InvalidParameters as ve:
        return (ve, None)

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

def filterAllTransactions(command, transactionPack):
    '''
    Function to return the filtered transaction, that is, all the 'in' tranasction or the 'out' transactions
    :param command:
    :param transactionList:
    :return: another list which is sublist of transactionList or None if there are exceptions
    '''
    try:
        arg = getAllArguments(command)
        return (None, [transaction for transaction in transactionPack[0] if transaction[2] == arg])
    except CommandError as se:
        return (se, None)
    except InvalidParameters as ve:
        return (ve, None)

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
        raise InvalidParameters("Balance - day should be integer!")
    if int(command[1]) <= 0:
        raise InvalidParameters("Balance - day should be positive!")
    return int(command[1])

def computeBalance(command, transactionPack):
    '''
    Function to compute the balance of the given day.
    :param command:
    :param transactionList:
    :return:an integer representing the balance up the the given day
    '''
    try:
        arg = getBalanceArguments(command)
        sum = 0
        for transaction in transactionPack[0]:
            if transaction[0] <= arg:
                if transaction[2] == 'in':
                    sum += transaction[1]
                else:
                    sum -= transaction[1]
        return sum
    except CommandError as se:
        return str(se)
    except InvalidParameters as ve:
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
        raise InvalidParameters("Sum command - Unknown transaction type!")
    return command[1]

def getSum(command, transactionPack):
    '''
    Function to return the sum for the given arguments
    :param command: the list containing the whitespace-split command from the user
    :param transactionList:
    :return: the sum of the filtere transactions
    '''
    try:
        arg = getSumArgument(command)
        return sum([transaction[1] for transaction in transactionPack[0] if transaction[2] == arg])
    except CommandError as se:
        return str(se)
    except InvalidParameters as ve:
        return str(ve)

def getMaxArguments(command):
    '''
    Function to get the arguments of Max command
    :param command: a list containing the whitespace-split command from the user
    :return: an string from the set {"in", "out"} which is the argument of the max command
    :raises exception whenever there is a syntax error, a value error or an invalid parameter error.
    '''
    if len(command) < 3:
        raise CommandError("Max command - Syntax error!")
    if command[1] != 'in' and command[1] != 'out':
        raise InvalidParameters("Max command - Unknown type of transaction")
    if command[2] != 'day':
        raise CommandError("Max command - Syntax error!")
    return command[1]

def getMax(command, transactionPack):
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
        for transaction in transactionPack[0]:
            if transaction[2] == args and maximum < transaction[1]:
                maximum = transaction[1]
                day = transaction[0]
        return day
    except CommandError as se:
        return str(se)
    except InvalidParameters as ve:
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

def sortTransactions(command, transactionPack):
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
                return (None, sorted(transactionPack[0], key = lambda transaction : transaction[1]))
            elif args[0] == 'desc':
                return (None, sorted(transactionPack[0], key = lambda transaction : transaction[1], reverse=True))
        else:
            if args[0] == 'asc':
                return (None, sorted([transaction for transaction in transactionPack[0] if transaction[2] == args[1]], key = lambda transaction : transaction[1]))
            else:
                return (None, sorted([transaction for transaction in transactionPack[0] if transaction[2] == args[1]], key = lambda transaction : transaction[1], reverse=True))
    except CommandError as se:
        return (se, None)
    except InvalidParameters as ve:
        return (ve, None)

def getFilterArguments(command):
    '''
    Function to return a list of arguments which represents the Filter command arguments
    :param command: a list of strings which is the input string split by whitespaces
    :return:
    '''
    if len(command) < 2:
        raise CommandError("Filter command - Syntax Error.")
    if command[1] != 'in' and command[1] != 'out':
        raise InvalidParameters("Filter command - the first parameter should be either in or out.")
    if len(command) > 2 and not representsInt(command[2]):
        raise InvalidParameters("Filter command - the second arguments should be an integer.")
    if len(command) > 2 and not int(command[2]) < 0:
        raise InvalidParameters("Filter command - the second arguments should be positive.")
    args = [command[1]]
    if len(command) > 2:
        args.append(command[2])
    return args

def filterTransaction(command, transactionPack):
    '''
    Function to return the 'filtered' transactions list, filters given by the arguments.
    :param command: a list of strings which is the input string split by whitespaces
    :param transactionList: the initial list
    :return: a new transaction list or None if there are exceptions
    '''
    try:
        args = getFilterArguments(command)
        if len(args) == 1:
           return (None, [transaction for transaction in transactionPack[0] if transaction[2] == args[0]])
        else:
            return (None, [transaction for transaction in transactionPack[0] if transaction[1] >= args[1] and transaction[2] == args[0]])
    except CommandError as ce:
        return (ce, None)
    except InvalidParameters as pe:
        return (pe, None)

def undo(transactionPack):
    '''
    Function to implement the undo feature of the Bank Account Management
    :param transactionPack: a tuple (list, historyList) of the transactions.
    :return: a new tuple, which is the updated one.
    '''
    if len(transactionPack[1]) == 0:
        return transactionPack
    if len(transactionPack) == 3:
        transactionPack[2] = (transactionPack[0][:])
    else:
        transactionPack.append(transactionPack[0][:])
    transactionPack[0] = transactionPack[1][-1]
    transactionPack[1] = transactionPack[1][0:-1]
    return transactionPack

def redo(transactionPack):
    '''
    Function to implement the redo feature of the Bank Account Management
    :param transactionPack: a tuple (list, historyList) of the transactions.
    :return: a new tuple, which is the updated one.
    '''
    if len(transactionPack) != 3:
        return transactionPack
    else:
        transactionPack[1].append(transactionPack[0])
        transactionPack[0] = transactionPack[2]
        transactionPack = transactionPack[:-1]
        return transactionPack