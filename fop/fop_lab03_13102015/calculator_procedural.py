"""
   A teacher (client) needs a program for students (users) who learn or use rational numbers.
  The program shall help students to make basic arithmetic operation
"""


def gcd(a, b):
    """
    Return the greatest common divisor of two positive integers.
    a,b integer numbers
    return an integer number, the  greatest common divisor of a and b
    """
    if a < 0 or b < 0:
        raise ValueError("a and b must be greater than 0")
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined")
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def rational_add(a1, a2, b1, b2):
    """
    Return the sum of two rational numbers.
    a1,a2,b1,b2 integer numbers, a2<>0 and b2<>0
    return a list with 2 integer numbers, representing a rational number a1/b2 + b1/b2
    Raise ValueError if the denominators are zero.
    """
    if a2 == 0 or b2 == 0:
        raise ValueError("0 denominator not allowed")
    c = [a1 * b2 + a2 * b1, a2 * b2]
    d = gcd(c[0], c[1])
    c[0] = c[0] / d
    c[1] = c[1] / d
    return c

def rational_multiply(a1, a2, b1, b2):
    """
    Return the product of two rational numbers.
    a1,a2,b1,b2 integer numbers, a2<>0 and b2<>0
    return a list with 2 integer numbers, representing a rational number a1/a2 * b1/b2
    Raise ValueError if the denominators are zero.
    """
    if a2 == 0 or b2 == 0:
        raise ValueError("0 denominator not allowed")
    c = [a1 * b1, a2 * b2]
    d = gcd(c[0], c[1])
    c[0] = c[0] / d
    c[1] = c[1] / d
    return c

def calc_get_total(calc):
    """
      Current total
      calc - calculator
      return a list with 2 elements representing a rational number
    """
    return calc[0]

def undo(calc):
    """
      Undo the last user operation
      calc - calculator
      post: restore the previous current total
    """
    undolist = calc[1]
    if len(undolist) == 0:
        return
    calc_total = undolist[-1]
    undolist = undolist[:-1]
    calc[0] = calc_total
    calc[1] = undolist

def calc_add(calc,a, b):
    """
      add a rational number to the current total
      calc - calculator
      a, b integer number, b<>0
      post: add a/b to the current total
    """
    undolist = calc[1]
    calc_total = calc[0]
    #add the current total to the undo list
    undolist.append(calc_total)
    #set the current rational number in the calc
    calc[0] = rational_add (calc_total[0], calc_total[1], a, b)

def calc_multiply(calc,a,b):
    undolist = calc[1]
    calc_total = calc[0]
    undolist.append(calc_total)
    #set the current rational number in the calc
    calc[0] = rational_multiply (calc_total[0], calc_total[1], a, b)

    


def reset_calc():
    """
      Create a new calculator
      post: the curent total equal 0/1
      return calculator
    """
    #we store here the curent total
    calc_total = [0, 1]
    #we store here a history of current totals (for undo)
    undolist = []
    return [calc_total,undolist]
    
    

def printMenu():
    """
      Print out the main menu of the calculator
    """
    print("Calculator menu:")
    print("   + for adding a rational number")
    print("   c to clear the calculator")
    print("   u to undo the last operation")
    print("   x to close the calculator")
    print("   * to multiply a rational number")

def printCurrent(calc):
    """
      Print the current total
      calc - calculator
    """
    print("Total:", calc_get_total(calc))
    
def multiplyToCalc(calc):
    """
      Read a rational number and add to the current total
      calc - calculator
    """
    m = input("Give nominator:")
    n = input("Give denominator:")
    try:
        calc_multiply(calc,int(m), int(n))
        printCurrent(calc)
    except ValueError:
        print ("Enter integers for m, n, with not null n")

def addToCalc(calc):
    """
      Read a rational number and add to the current total
      calc - calculator
    """
    m = input("Give nominator:")
    n = input("Give denominator:")
    try:
        calc_add (calc,int(m), int(n))
        printCurrent(calc)
    except ValueError:
        print ("Enter integers for m, n, with not null n")

def run():
    """
      Implement the user interface
    """
    calc = reset_calc()
    finish = False
    printCurrent(calc)
    while not finish:
        printMenu()
        m = input().strip()
        if (m == 'x'):
            finish = True
        elif (m == '+'):
            addToCalc(calc)
        elif (m=='c'):
            calc = reset_calc()
            printCurrent(calc)
        elif (m=='u'):
            undo(calc)
            printCurrent(calc)
        elif m == '*':
            multiplyToCalc(calc)
        else:
            print("Invalid command")

    print ("Bye!!!")


### test cases

def test_gcd():
    """
      test function for gdc
    """
    assert gcd(0, 2) == 2
    assert gcd(2, 0) == 2
    assert gcd(2, 3) == 1
    assert gcd(2, 4) == 2
    assert gcd(6, 4) == 2
    assert gcd(24, 9) == 3
    try:
        gcd(-2, 0)
        gcd(0, -2)
        gcd(0, 0)
        assert False
    except ValueError:
        assert True

def test_rational_add():
    """
      Test function for rational_add
    """
    assert rational_add(1, 2, 1, 3) == [5, 6]
    assert rational_add(1, 2, 1, 2) == [1, 1]

def test_calculator_add():
    """
      Test function for calculator_add
    """
    calc = reset_calc()
    assert calc_get_total(calc) == [0, 1]
    calc_add(calc,1, 2)
    assert calc_get_total(calc) == [1, 2]
    calc_add(calc,1, 3)
    assert calc_get_total(calc) == [5, 6]
    calc_add(calc,1, 6)
    assert calc_get_total(calc) == [1, 1]

def test_undo():
    """
      Test function for undo
    """
    calc = reset_calc()
    calc_add(calc,1, 3)
    undo(calc)
    assert calc_get_total(calc) == [0, 1]
    calc = reset_calc()
    calc_add(calc,1, 3)
    calc_add(calc,1, 3)
    calc_add(calc,1, 3)
    undo(calc)
    assert calc_get_total(calc) == [2, 3]


#run the test - invoke the test function
test_gcd()

test_rational_add()
test_calculator_add()
test_undo()

run()
