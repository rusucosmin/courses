__author__ = 'cosmin'

import datetime

class SyntaxError(Exception):
    pass

class InvalidParameters(Exception):
    pass

def displayStartMenu():
    '''
    Function to display the START MENU
    '''
    actualTime = datetime.datetime.now()
    print("Today's date: " + str(actualTime.date().day))
    print("Hello. Please insert a command. Type 'help' to show menu")

def clearWindow():
    '''
    Function to clear the terminal in Ubuntu
    '''
    print(chr(27) + "[2J")

def displayCommands():
    '''
    Function to display all the functionalities of the application.
    '''
    clearWindow()

    print("Here are all the command you can use:")
    print("     list - displays the list of all transactions")
    print("     add X,Y,description - adds to the current day an in/out transaction of X RON with the given description")
    print("     insert X, Y, in/out, description – inserts in day X an in/out transaction of Y RON with the given description")
    print("     remove X – removes all the transactions from day X")
    print("     remove from X to Y – removes all the transactions from day X until day Y")
    print("     remove in/out – removes all the in/out transactions from the current month")
    print("     replace X, in/out, description with Y – replaces the amount for the in/out transaction having the specified description from day X with Y RON")
    print("     exit - to quit the application")

def printTransactions(transactionList):
    '''
    function to show all the transactions stored in the application
    :param  transactionList: the list of transaction
            each transaction is, in fact, a touple (day-integer, amount of money - integer, transaction type - can be "in" or "out", description - string
    '''
    if transactionList is None or len(transactionList) == 0:
        print("There are no transactions made!")
    else:
        print("These are the stored transactions:")
        for i in range(len(transactionList)):
            print(str(1 + i) + ". " + ', '.join([str(x) for x in transactionList[i]]))

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
        return False

def getAddTransaction(command):
    '''
    A function to handle the Add Transaction Feature

    :param command: the command the user has inputted
    :return a tuple (day, amount, in/out, description) which describes
                the transaction the user wants to add
            or None if there is a command syntax error
    '''
    if len(command) < 2:
        raise SyntaxError("Add command - Syntax Error!")
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
    except SyntaxError as se:
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
        raise SyntaxError("Insert Command - Syntax Error!")
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

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    newTransaction = None
    try:
        newTransaction = getInsertTransaction(command)
    except ValueError as ve:
        print(str(ve))
    except SyntaxError as se:
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
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    day = None
    try:
        day = getRemoveTransactionDay(command)
    except ValueError as ve:
        print(str(ve))
    except SyntaxError as se:
        print(str(se))
    except InvalidParameters as ie:
        print(str(ie))
    return [transaction for transaction in transactionList if transaction[0] != day]

def getRemoveTransactionInterval(command, transactionList):
    if command[1] != 'from' or command[3] != 'to':
        raise SyntaxError("Remove command - Syntax Error!")
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

    (startDate, endDate) = getRemoveTransactionInterval(command)
    return [transaction for transaction in transactionList if not startDate <= transaction[0] <= endDate]

def getRemoveTypeTransaction(command):
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
        arg = getRemoveTransactionDay(command)
    except ValueError as ve:
        print(str(ve))
    return [transaction for transaction in transactionList if transaction[2] != arg]

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
    if len(command) < 4:
        raise SyntaxError("Replace command - Syntax error!")
    if command[-2] != 'with':
        raise SyntaxError("Replace command - Syntax error!")
    if representsInt(command[-1]) == False:
        raise ValueError("Replace command - Amount not an integer!")
    if int(command[-1]) <= 0:
        raise ValueError('Replace command - Amount cannot be negative or null!')
    argsList = command[1].split(',')
    if len(argsList) < 3:
        raise SyntaxError("Replace command - Not enough parameters!")
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
        description = description + ' ' + ' '.join(command[3:-3])
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
    except SyntaxError as se:
        print(str(se))
    except InvalidParameters as ie:
        print(str(ie))
    for i in range(len(transactionList)):
        if transactionList[i][0] == day and transactionList[i][2] == type and transactionList[i][3] == description:
            transactionList[i] = (transactionList[i][0], newAmount, transactionList[i][2], transactionList[i][3])
    return transactionList

def getCommand():
    '''
    Function to get the command from the user.

    :return: a list of string, containing the command splitted by the whitespaces
    '''
    userInput = input("> ")
    command = userInput.split(" ")
    return command

def main():
    '''
    This is the function that controls the whole application.
    :return:
    '''
    transactionList = None #todo: getTheTransactionList from a file or db
    displayStartMenu()
    while True:
        if transactionList is None:
            transactionList = []
        command = getCommand()
        if len(command) == 0:
            continue
        if command[0] == "help":
            displayCommands()
        elif command[0] == "list":
            printTransactions(transactionList)
        elif command[0] == "add":
            transactionList = addTransaction(command, transactionList)
        elif command[0] == "insert":
            transactionList = insertTransaction(command, transactionList)
        elif command[0] == "remove":
            transactionList = removeTransaction(command, transactionList)
        elif command[0] == "replace":
            transactionList = replaceTransaction(command, transactionList)
        elif command[0] == "exit":
            print("Exiting")
            break
        else:
            print('command not recognized')

if __name__ == '__main__':
    main()