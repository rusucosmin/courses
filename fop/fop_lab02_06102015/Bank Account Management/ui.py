__author__ = 'cosmin'

from commands import *

def displayStartMenu():
    '''
    Function to display the START MENU
    '''
    print("Hello. Please insert a command. Type 'help' to show menu")

def clearWindow():
    '''
    Function to clear the terminal in Ubuntu
    '''
    print(chr(27) + "[2J")

def displayCommands():
    '''
    Function to display all the functionality of the application.
    '''
    clearWindow()

    print("Here are all the command you can use:")
    print("    list - displays the list of all transactions")
    print("    add X,in/out,description - adds to the current day an in/out transaction of X RON with the given description")
    print("    insert X, Y, in/out, description – inserts in day X an in/out transaction of Y RON with the given description")
    print("    remove X – removes all the transactions from day X")
    print("    remove from X to Y – removes all the transactions from day X until day Y")
    print("    remove in/out – removes all the in/out transactions from the current month")
    print("    replace X, in/out, description with Y – replaces the amount for the in/out transaction having the specified description from day X with Y RON")
    print("    exit - to quit the application")

def printTransactions(transactionList):
    '''
    function to show all the transactions stored in the application
    :param  transactionList: the list of transaction
            each transaction is, in fact, a tuple (day-integer, amount of money - integer, transaction type - can be "in" or "out", description - string
    '''
    if transactionList is None:
        return
    if len(transactionList) == 0:
        print("There are no transactions made!")
    else:
        print("These are the stored transactions:")
        for i in range(len(transactionList)):
            print(str(1 + i) + ". " + ', '.join([str(x) for x in transactionList[i]]))

def getCommand():
    '''
    Function to get the command from the user.

    :return: a list of string, containing the command splitted by the whitespaces
    '''
    userInput = input("> ")
    command = userInput.split(" ")
    return command

def runUi():
    transactionList = [(1, 100, "in", "cosmin"), (2, 1000, "out", "description"), (3, 150, "in", "ok"), (15, 123, "out", "salary"), (17,2000,"in","a year salary"), (11,2500, "in", "saled the car"), (11,5000,"out", "bought a macbook")] #todo: getTheTransactionList from a file or db
    displayStartMenu()
    while True:
        if transactionList is None:
            transactionList = []
            print('transactionlist was none')
        command = getCommand()
        if len(command) == 0:
            continue
        if command[0] == "help":
            displayCommands()
        elif command[0] == "list" or command[0] == 'ls':
            printTransactions(transactionList)
        elif command[0] == "add":
            transactionList = addTransaction(command, transactionList)
        elif command[0] == "insert":
            transactionList = insertTransaction(command, transactionList)
        elif command[0] == "remove":
            transactionList = removeTransaction(command, transactionList)
        elif command[0] == "replace":
            transactionList = replaceTransaction(command, transactionList)
        elif command[0] == "greater" or command[0] == "less":
            printTransactions(filterPropertyTransactions(command, transactionList))
        elif command[0] == "all":
            printTransactions(filterAllTransactions(command, transactionList))
        elif command[0] == "balance":
            print("Balance on the given day was ", computeBalance(command, transactionList))
        elif command[0] == "sum":
            print(getSum(command, transactionList))
        elif command[0] == "max":
            print(getMax(command, transactionList))
        elif command[0] == "asc" or command[0] == "desc":
            printTransactions(sortTransactions(command, transactionList))
        elif command[0] == "exit":
            print("Exiting")
            break
        else:
            print('command not recognized')
