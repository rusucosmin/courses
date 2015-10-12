__author__ = 'cosmin'

import datetime

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
    :rtype : boolean1
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
        print("invalid syntax")
        return None
    argsList = command[1].split(',')
    if len(argsList) < 3:
        print("not enough parameters, please input the amount, the type (in/out) and the description")
        return None
    if representsInt(argsList[0]) == False:
        print("amount not an integer")
        return None
    if int(argsList[0]) <= 0:
        print('amount cannot be negative or nul')
        return None
    if argsList[1].lower() not in ["in", "out"]:
        print('the only known transaction types are in and out')
        return None
    description = ','.join(argsList[2:])
    if len(command) > 2:
        description = description + ' ' + ' '.join(command[2:])
    transaction = (datetime.datetime.now().day, int(argsList[0]), argsList[1], description)
    return transaction

def getInsertTransaction(command):
    '''
    A function to handle the Insert Transaction Feature

    :param command: the command the user has inputted
    :return a tuple (day, amount, in/out, description) which describes
                the transaction the user wants to insert
            or None if there is a command syntax error
    '''
    if len(command) < 2:
        print('invalid syntax')
        return None
    argsList = command[1].split(',')
    if len(argsList) < 4:
        print('not enough parameters, please input the day, amount, the type(in/out) and the description')
    if representsInt(argsList[0]) == False:
        print('day not an integer')
    if int(argsList[0]) <= 0:
        print('day cannot be negative or nul')
        return None
    if representsInt(argsList[1]) == False:
        print('amount not an integer')
    if int(argsList[1]) <= 0:
        print('amount cannot be negative or nul')
        return None
    if argsList[2].lower() not in ["in", "out"]:
        print('the only known transaction types are in and out')
        return None
    description = ','.join(argsList[3:])
    if len(command) > 2:
        description = description + ' ' + ' '.join(command[2:])
    transaction = (int(argsList[0]), int(argsList[1]), argsList[2], description)
    return transaction

def addTransaction(command, transactionList):
    '''
    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    newTransaction = getAddTransaction(command)
    if newTransaction is not None:
        transactionList.append(newTransaction)
    return transactionList

def insertTransaction(command, transactionList):
    '''
    Function to update the list with the correct new insert transaction

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    newTransaciton = getInsertTransaction(command)
    if newTransaciton is not None:
        transactionList.append(newTransaciton)
    return transactionList

def removeTransactionDay(command, transactionList):
    '''
    Function to remove all the transaction from a specific day

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    if representsInt(command[1]) == False:
        print("Day is not an interger")
        return transactionList
    if int(command[1]) <= 0:
        print("Day cannot be negative or null")
        return transactionList
    day = int(command[1])
    return [transaction for transaction in transactionList if transaction[0] != day]

def removeTransactionInterval(command, transactionList):
    '''
    Function to remove all the transaction from a specific interval of days

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    if command[1] != 'from' or command[3] != 'to':
        print("invalid syntax")
        return transactionList
    if representsInt(command[2]) == False or representsInt(command[4]) == False:
        print("Day is not an interger")
        return transactionList
    if int(command[2]) <= 0:
        print("Day cannot be negative or null")
        return transactionList
    startDate = int(command[2])
    endDate = int(command[4])
    if startDate > endDate:
        print("Not an interval of dates")
        return transactionList
    return [transaction for transaction in transactionList if not startDate <= transaction[0] <= endDate]

def removeTypeTransaction(command, transactionList):
    '''
    Function to remove all the transaction with the type given by user (in / out)

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''
    if command[1] != 'in' and command[1] != 'out':
        return transactionList
    return [transaction for transaction in transactionList if transaction[2] != command[1]]

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

def replaceTransaction(command, transactionList):
    '''
    Function to replace a transaction's amount of money.

    :param command: a list representing the command the user wants to make, which is the string splitted by spaces
    :param transactionList: a list of touples where each transaction are stored
    :return: a new transaction list which is the updated one, if the command is correctly inputted, or transactionList if the command is not good
    '''

    if len(command) < 4:
        print("command syntax error")
        return transactionList
    if command[-2] != 'with':
        print("command syntax error")
        return transactionList
    if representsInt(command[-1]) == False:
        print("amount not an integer")
        return transactionList
    argsList = command[1].split(',')
    if len(argsList) < 3:
        print("not enough arguments")
        return transactionList
    if representsInt(argsList[0]) == False:
        print("date not an integers")
        return transactionList
    if int(argsList[0]) <= 0:
        print("date cannot be negative or nul")
        return transactionList
    if argsList[1] not in ['in', 'out']:
        print("transaction type unknown, should be only in or out")
        return transactionList


    newAmount = int(command[-1])
    day = int(argsList[0])
    description = ','.join(argsList[2:])
    if len(command) > 4:
        description = description + ' ' + ' '.join(command[3:-3])

    for i in range(len(transactionList)):
        if transactionList[i][0] == day and transactionList[i][2] == argsList[1] and transactionList[i][3] == description:
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
        if transactionList == None:
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
        else:
            print('command not recognized')

if __name__ == '__main__':
    main()