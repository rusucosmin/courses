from model.integer import Integer
from model.exceptions import IntegerException

class Calculator:
    '''
    Class to control the whole UI interaction.

    Calculator.Menu = a list of all allowed type of operations the user can use
    '''
    Menu = [1, 2, 3, 4, 5]
    def __init__(self, controller):
        self._controller = controller

    def printMainMenu(self):
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division with one digit")
        print("5. conversion")

    def getInteger(self):
        base = int(input("Insert base: "))
        s = input("Insert number representation: ")
        return Integer(base, s)

    def getOperands(self):
        x = self.getInteger()
        y = self.getInteger()
        return x, y

    def run(self):
        while True:
            try:
                self.printMainMenu()
                op = int(input("Please input the type of operation you want to do: "))
                if op == 1:
                    x, y = self.getOperands()
                    print(x + y)
                elif op == 2:
                    x, y = self.getOperands()
                    print(x - y)
                elif op == 3:
                    x, y = self.getOperands()
                    print(x * y)
                elif op == 4:
                    x = self.getInteger()
                    y = self.getOneDigitInteger()
                    print("quotient: ", x // y)
                    print("remainder: ", x % y)
                elif op == 5:
                    x = self.getInteger()
                    y = int(input("Input the destination base: "))
                    print(x.convertToBase(y))
            except ValueError:
                print("Value should be integer.")
            except IntegerException as ie:
                print(ie)