from model.integer import Integer
from model.exceptions import IntegerException

# ===Calculator class===

class Calculator:
    """
    Class to control the whole UI interaction.
    Properties:

    **Calculator.Menu** - a list of all allowed type of operations the user can use
    """
    Menu = [1, 2, 3, 4, 5, 6]
    def __init__(self):
        '''
        Class constructor
        '''
        pass

    def printMainMenu(self):
        '''
        Function to print the main menu
        '''
        print("\nBase Calculator\n")
        print("Computational logic optional homework project")
        print("Author: Cosmin Rusu\n")

        print("Here is what you can do:")
        print("     1. addition")
        print("     2. subtraction")
        print("     3. multiplication")
        print("     4. division with one digit")
        print("     5. conversion")
        print("     6. exit")
        print("")

    def getInteger(self):
        '''
        Function to read a number from the user
        :return: the number the user gave
        '''
        base = int(input("Insert base: "))
        s = input("Insert number representation: ")
        return Integer(base, s)

    def getOperands(self):
        '''
        Function to get two numbers from the user
        '''
        x = self.getInteger()
        y = self.getInteger()
        return x, y

    def waitToContinue(self):
        input("Press any key to continue...")

    def getOneDigitInteger(self):
        x = input("Please insert a one-digit number: ")
        while not x in Integer.Values.keys():
            x = input("Please insert a one-digit number: ")
        x = Integer.Values[x]
        return x

    def run(self):
        '''
        Function to handle the user interactions
        '''
        while True:
            try:
                self.printMainMenu()
                op = int(input("Please input the type of operation you want to do: "))
                if op == 1:
                    x, y = self.getOperands()
                    print("\nHere is the result: ")
                    print(x, " + ", y, " = ", x + y)
                elif op == 2:
                    x, y = self.getOperands()
                    print("\nHere is the result: ")
                    print(x, " - ", y, " = ", x - y)
                elif op == 3:
                    x, y = self.getOperands()
                    print("\nHere is the result: ")
                    print(x, " * ", y, " = ", x * y)
                elif op == 4:
                    x = self.getInteger()
                    y = self.getOneDigitInteger()
                    print("\nHere is the result: ")
                    print(x, " / ", y, " = ", x // y, ", remainder ", Integer(x.getBase(), Integer.Symbols[x % y]))
                elif op == 5:
                    x = self.getInteger()
                    y = int(input("Input the destination base: "))
                    print("\nHere is the result: ")
                    print(x, " = ", x.convertToBase(y))
                elif op == 6:
                    print("Thank you for using this software. Have a nice day!\nCosmin Rusu")
                    break;
                else:
                    print("\n\nPlease choose only 1, 2, 3, 4 or 5.\n\n")
            except ValueError:
                print("\n\nValue should be integer.\n\n")
            except IntegerException as ie:
                print("\n\n" + str(ie) + "\n\n")
            except Exception as e:
                print("\n\n" + str(e) + "\n\n")
            self.waitToContinue()