__author__ = 'cosmin'

import datetime

def clearWindow():
    print(chr(27) + "[2J")

def displayMainMenu():
    '''
    This function shows the application operation
    :return:
    '''
    clearWindow();
    actualTime = datetime.datetime.now()
    print("Hello\nToday's date is " + str(actualTime.day))
    print("Insert 1 to add a new transaction.")
    print("Insert 2 to modify transactions from the list.")
    print("Insert 3 to exit Application.")

def displayAddMenu():
    clearWindow();
    print("Insert 1 to add an out transaction to the current day.")
    print("Insert 2 to insert an in transaction.")
    print("Insert 3 to go back to main menu")

def displayModifyMenu():
    clearWindow();
    print("1. Remove all the transactions from a specific day")
    print("2. Remove all the transactions from a specific interval of days")
    print("3. Remove all the in transaction")
    print("4. Replace a transaction's amount of money")
    print("5. Go back to main menu")

def printTransactions(transactionList):
    if transactionList is None or len(transactionList) == 0:
        print("There are no transactions made!")
    else:
        print(transactionList)

def getOperationType(allowedTypes):
    '''
    This function returns the type of operation the user chosen from the allowedTypes list
    :param allowedTypes : a list containing the ids of the operation the user can chose
    :return an integer representing the operation number
    '''
    userInput = input("Please input the number of operation you want to make: ")
    while representsInt(userInput) == False or int(userInput) not in allowedTypes:
        userInput = input("Please input a valid type of transaction from menu: ")
    return int(userInput)

def getAmount():
    userInput = input("Please input the amount of money for the transaction: ")
    while representsInt(userInput) == False or int(userInput) <= 0: #no 0-amount transaction is allowed
        userInput = input("Please input the amount of money for the transaction: ")
    return int(userInput)

def getDescription():
    userInput = input("Please input a description of the transaction: ")
    return userInput

def getDate():
    userInput = input("Please input the date when the transaction was made: ")
    while representsInt(userInput) == False:
        userInput = input("Please input the date when the transaction was made: ")
    return int(userInput)

def getType():
    userInput = input("Input transaction type (in/out)")
    while userInput != 'in' and userInput != 'out':
        userInput = input("Input transaction type (in/out)")
    return userInput

def getAddTransaction():
    '''
    A function to handle the Add Transaction Feature

    :return a tuple (day, amount, in/out, description) which describes
                the addTransaction the user wants to do
    '''
    displayAddMenu()
    addOperationType = getOperationType([1, 2, 3])
    print("You inserted", addOperationType)
    if addOperationType == 1:
        transaction = (datetime.datetime.now().day, getAmount(), "out", getDescription())
        return transaction
    elif addOperationType == 2:
        transaction = (getDate(), getAmount(), "in", getDescription())
        return transaction
    else:
        return None

def representsInt(s):
    '''

    function to return True if the :param s is an integer
    :param s: the input user has given
    :rtype : boolean1
    :return: True if s is an integer
             False is s is not an integer
    '''
    try:
        int(s)
        return True
    except ValueError:
        return False

def addTransaction(transactionList):
    newTransaction = getAddTransaction()
    if newTransaction is not None:
        transactionList.append(newTransaction)
    return transactionList

def removeTransactionDay(transactionList):
    transactionDay = getDate()
    return [transaction for transaction in transactionList if transaction[0] != transactionDay]

def removeTransactionInterval(transactionList):
    startDate = getDate()
    endDate = getDate()
    while startDate > endDate:
        print("Not an interval")
        endDate = getDate()
    return [transaction for transaction in transactionList if not startDate <= transaction[0] <= endDate]

def removeInTransaction(transactionList):
    return [transaction for transaction in transactionList if transaction[2] != 'in']

def replaceTransaction(transactionList):
    print("Please input the day, type and description for the transaction you want to update")
    day = getDate()
    type = getType()
    description = getDescription()

    while len([transaction for transaction in transactionList if transaction[0] == day and transaction[2] == type and transaction[3] == description]) == 0:
        print("No such update exists, please input the day, type and description for the transaction you want to update")
        day = getDate()
        type = getType()
        description = getDescription()

    newAmount = input("Input new amount:")

    for i in range(len(transactionList)):
        if transactionList[i][0] == day and transactionList[i][2] == type and transactionList[i][3] == description:
            transactionList[i] = (transactionList[i][0], newAmount, transactionList[i][2], transactionList[i][3])

    return transactionList

def modifyTransaction(transactionList):
    displayModifyMenu()
    modifyTransactionType = getOperationType([1, 2, 3, 4, 5])
    if modifyTransactionType == 1:
        transactionList = removeTransactionDay(transactionList)
    elif modifyTransactionType == 2:
        transactionList = removeTransactionInterval(transactionList)
    elif modifyTransactionType == 3:
        transactionList = removeInTransaction(transactionList)
    elif modifyTransactionType == 4:
        transactionList = replaceTransaction(transactionList)
    return transactionList

def assertions():
    assert representsInt(getDate()) == True
    assert representsInt(getAmount()) == True
    assert representsInt(getType())

def main():
    '''
    This is the function that controls the whole application.
    :return:
    '''
    transactionList = None #todo: getTheTransactionList from a file or db

    while True:
        displayMainMenu()
        if transactionList is None:
            transactionList = []
        printTransactions(transactionList)
        operationType = getOperationType([1, 2, 3])
        if operationType == 1:
            transactionList = addTransaction(transactionList)
        elif operationType == 2:
            transactionList = modifyTransaction(transactionList)
        elif operationType == 3:
            clearWindow()
            print("Exiting application...")
            break

if __name__ == '__main__':
    main()