__author__ = 'cosmin'

from commands import *

def displayStartMenu():
    '''
    Function to display the START MENU
    '''
    print("Hello. Please insert a command. Type 'help' to show menu.")

def clearWindow():
    '''
    Function to clear the terminal in Ubuntu
    '''

def displayCommands():
    '''
    Function to display all the functionality of the application.
    '''
    clearWindow()

    print("Here are all the command you can use:")
    print("     'list' - displays the list of all transactions")
    print("     'add X,in/out,description' - adds to the current day an in/out transaction of X RON with the given description")
    print("     'insert X,Y,in/out,description' – inserts in day X an in/out transaction of Y RON with the given description")
    print("     'remove X' – removes all the transactions from day X")
    print("     'remove from X to Y' – removes all the transactions from day X until day Y")
    print("     'remove in/out' – removes all the in/out transactions from the current month")
    print("     'replace X,in/out,description with Y' – replaces the amount for the in/out transaction having the specified description from day X with Y RON")
    print("     'greater than X' - writes all transactions greater than X")
    print("     'less than X before Y' - writes all transactions less than X which were made before day Y")
    print("     'all in/out' – writes all the in transactions.")
    print("     'balance X' – computes the account’s balance on day X - should be integer")
    print("     'sum in/out' – writes the total amount from in transactions")
    print("     'max out day' – writes the day with the maximum amount in an out transaction")
    print("     'asc sort day' – sorts the total daily transactions in an ascending order")
    print("     'desc sort type' - sorts the total daily transactions per type (in/out) in a descending order")
    print("     'filter in/out' - filters the transaction so that only the in/out will remain")
    print("     'undo' - undo the last operation")
    print("     'redo' - redo the last operation - currently supporting only one redo at a time")
    print("     'exit' - to quit the application")

def printTransactions(transactionPack):
    '''
    function to show all the transactions stored in the application
    :param  transactionList: the list of transaction
            each transaction is, in fact, a tuple (day-integer, amount of money - integer, transaction type - can be "in" or "out", description - string
    '''
    if transactionPack[0] is None:
        return
    transactionList = transactionPack[0]
    if transactionList is None:
        return
    if len(transactionList) == 0:
        print("There are no transactions made!")
    else:
        print("These are the transactions:")
        for i in range(len(transactionList)):
            print(str(1 + i) + ". " + ', '.join([str(x) for x in transactionList[i]]))

def printTransactionList(transactionPair):

    if transactionPair[0] is None:
        print("Here is the result of the query:")
        for i in range(len(transactionPair[1])):
            print(str(1 + i) + ". " + ', '.join([str(x) for x in transactionPair[1][i]]))
    else:
        print(str(transactionPair[0]))

def getCommand():
    '''
    Function to get the command from the user.

    :return: a list of string, containing the command splitted by the whitespaces
    '''
    userInput = input("> ")
    command = userInput.split(" ")
    return command

def printError(exception):
    print(str(exception))

def handleNewList(transactionPack, newList):
    if newList[0] is None:
        return newList[1]
    else:
        printError(newList[0])
        return transactionPack

def handleFilteredList(newList):
    if newList[0] is None:
        printTransactions(newList[1])
    else:
        printError(newList[0])

def printHistory(transactionPack):
    for list in transactionPack[1]:
        print(list)

def runUi():
    transactionPack = [[(1, 100, "in", "cosmin"), (2, 1000, "out", "description"), (3, 150, "in", "ok"), (15, 123, "out", "salary"), (17,2000,"in","a year salary"), (11,2500, "in", "saled the car"), (11,5000,"out", "bought a macbook")], []] #todo: getTheTransactionList from a file or db
    #transactionPack = [[(1,1,'in','a'), (2,2,'in','b'), (3,3,'in','c'), (4,4,'out','d'), (5,5,'in','e')], []]
    #transactionPack = [[], []]
    #todo add the transactions having the same values
    displayStartMenu()
    while True:
        #printHistory(transactionPack)
        #transactionList = transactionPack[0]
        command = getCommand()
        if len(command) == 0:
            continue
        if command[0] == "help":
            displayCommands()
        elif command[0] == "list" or command[0] == 'ls':
            printTransactions(transactionPack)
        elif command[0] == "add":
            newList = addTransaction(command, transactionPack)
            transactionPack = handleNewList(transactionPack, newList)
        elif command[0] == "insert":
            newList = insertTransaction(command, transactionPack)
            transactionPack = handleNewList(transactionPack, newList)
        elif command[0] == "remove":
            newList = removeTransaction(command, transactionPack)
            transactionPack = handleNewList(transactionPack, newList)
        elif command[0] == "replace":
            newList = replaceTransaction(command, transactionPack)
            transactionPack = handleNewList(transactionPack, newList)
        elif command[0] == "greater" or command[0] == "less":
            printTransactionList(filterPropertyTransactions(command, transactionPack))
        elif command[0] == "all":
            printTransactionList(filterAllTransactions(command, transactionPack))
        elif command[0] == "balance":
            print("Balance on the given day was ", computeBalance(command, transactionPack), ".")
        elif command[0] == "sum":
            print(getSum(command, transactionPack))
        elif command[0] == "max":
            print(getMax(command, transactionPack))
        elif command[0] == "asc" or command[0] == "desc":
            printTransactionList(sortTransactions(command, transactionPack))
        elif command[0] == "filter":
            newList = filterTransaction(command, transactionPack)
            transactionPack = handleNewList(transactionPack, newList)
        elif command[0] == "undo":
            transactionPack = undo(transactionPack)
        elif command[0] == "redo":
            transactionPack = redo(transactionPack)
        elif command[0] == "h":
            printHistory(transactionPack)
        elif command[0] == "exit":
            print("Exiting...")
            break
        else:
            print("Command not recognized. Try 'help'!")