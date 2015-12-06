from copy import deepcopy

__author__ = 'cosmin'

from model.exceptions import IntegerException


class Integer:
    '''
    Class to represent a number

    self._length:   -the number of digits
    self._digits:   -the list of the number's digits
                    -the less significant digits are on the lower index of the array
    self._base :    -the base of the number
    '''
    AllowedBases = [2, 3, 4, 5, 6, 7, 8, 9, 10, 16]
    Values = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    Symbols = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    def __init__(self, base, number_repr):
        '''
        Constructor for the Integer class
        :param base: an integer - the base in which the number is represented
        :param number_repr: a string - the representation of the number in that base
        :raises IntegerException if the base is not one of the allowed base
        :raises IntegerException if the number has less than one digit
        '''
        if base not in Integer.AllowedBases:
            raise IntegerException("Not allowed base.")
        if number_repr == "":
            raise IntegerException("Number should have at least one digit.")
        self._base = base
        self._length = 0
        self._digits = []
        for ch in number_repr[::-1]:
            if not ch in Integer.Values.keys():
                raise IntegerException("Unknown base symbols.")
            if Integer.Values[ch] >= base:
                raise IntegerException("Unknown base symbols.")
            self.append(Integer.Values[ch])

    def valueOf(number_repr):
        '''
        Function to get the value of a symbol (digit)
        :return: the value of the symbol (digit) number_repr
        :raises: ValueError if the symbol is not recognised
        '''
        if number_repr in Integer.Values.keys():
            return Integer.Values[number_repr]
        raise ValueError("Not a digit...")

    def append(self, value):
        '''
        Function to append a digit to the most significant position
        :param: value:the value of the appended digit
        '''
        self._digits.append(value)
        self._length += 1

    def __repr__(self):
        '''
        Converts the number in it's representation in base self._base
        :return: a string - the representation of the number
        '''
        self.clearIsb()
        number_repr = ""
        for digit in self._digits[::-1]:
            number_repr += Integer.Symbols[digit]
        if number_repr == "":
            number_repr = "0"
        return number_repr

    def __str__(self):
        '''
        Same as __repr__, but much more human-readable (it also contains the base in parenthesis)
        :return: a string - the representation of the number
        '''
        return repr(self) + " (" + str(self._base) + ")"

    def clearIsb(self):
        '''
        Removes the leading zeros from the number. Function needed for the basic operations to make sense.
        Ex: 1999 - 1000 = 999 (not 0999)
        '''
        while len(self) > 0 and self[-1] == 0:
            self._digits.pop()
            self._length -= 1

    def __getitem__(self, item):
        '''
        Getter for the [] operator
        Ex: x = Integer(10, 12345)
        print(x[0]) will print the unit digit of the number
        :param: item: an integer - the position of the digit we want to obtain
        :return: an integer - the value of the digit at position item (0-indexed array)
        :raises: IndexError if the index is not within the index range of the number
        '''
        if item >= self._length:
            raise IndexError("Index out of range.")
        return self._digits[item]

    def __setitem__(self, key, value):
        '''
        Setter for the [] operator
        Ex: x = Integer(10, 12345)
        x[0] = 0 will put on the unit digit of the number the value 0
        :param: key: an integer - the position of the digit we want to obtain
        :param: value: an integer - the new value for the digit
        :return: an integer - the value of the digit at position item (0-indexed array)
        :raises: IndexError if the index is not within the index range of the number
        '''
        if key >= self._length:
            raise IndexError("Index out of range.")
        self._digits[key] = value

    def __len__(self):
        '''
        Function to return the number of digits in the number
        :return: an integer - the number of digits on the representation of the number in base self._baseX
        '''
        return self._length

    def getBase(self):
        '''
        Getter for the base of the number
        :return: an integer: the self._base property of the number
        '''
        return self._base

    def __add__(self, other):
        '''
        Function to implement the addition on two Integer objects
        :param other - the second operand of addition (the first one is self)
        :return an Integer representing the sum of self and other
        :raises ValueError if other is not of type Integer or if they are not in the same base
        '''
        if not isinstance(other, Integer):
            raise ValueError("Error - Addition on two different objects.")
        if self._base != other._base:
            raise ValueError("Error - Addition on two Integers with different bases.")
        base = self.getBase()
        new = Integer(base, repr(self))
        if len(new) < len(other):
            for i in range(0, len(other) - len(new)):
                new.append(0)
        else:
            for i in range(0, len(new)- len(other)):
                other.append(0)
        t = 0 #will handle the transport
        for i in range(0, new._length):
            val = new[i] + other[i] + t
            new[i] = val % base
            t = val // base
        if t:
            new.append(t)
        return new

    def __sub__(self, other):
        '''
        Function to implement the subtraction of an Integer from self.
        :param other - the subtrahend of subtraction (the Minuend is self)
        :return an Integer representing the difference between self and other
        :raises ValueError if other is not of type Integer or if they are not in the same base
        '''
        if not isinstance(other, Integer):
            raise ValueError("Error - Subtraction on two different objects.")
        if self.getBase() != other.getBase():
            raise ValueError("Error - Subtraction on two numbers with different bases.")
        new = Integer(self._base, repr(self))
        t = 0
        for i in range(len(new) - len(other)):
            other.append(0)

        for i in range(0, len(self)):
            new[i] = new[i] - (other[i] + t)
            if new[i] < 0:
                t = 1
            else:
                t = 0
            if t:
                new[i] += new.getBae()

        new.clearIsb()
        return new

    def __mul__(self, other):
        '''
        Function to implement the multiplication of an Integer with another Integer
        :param other - the Multiplier (the Multiplicand is self)
        :return an Integer representing the product of self and other
        :raises ValueError if other is not of type Integer or if they are not in the same base
        '''
        if not isinstance(other, Integer):
            raise ValueError("Error - Multiplication only allowed between Integers.")
        if self.getBase() != other.getBase():
            raise ValueError("Error - Multipliaction on Integers with different bases.")
        new = Integer(self._base, "0" * (len(self) + len(other) - 1))
        t = 0
        for i in range(0, len(self)):
                for j in range(0, len(other)):
                    new[i + j] += self[i] * other[j]
        for i in range(0, len(new)):
            new[i] += t
            t = new[i] // self.getBase()
            new[i] = new[i] % self.getBase()

        while t > 0:
            new.append(t % self._base)
            t = t // self._base

        return new

    def __floordiv__(self, other):
        '''
        Function to implement the division of an Integer with a one digit Integer
        :param other - the Divisor (the Dividend is self)
        :return an Integer representing the quotient of the division of self and other
        :raises ValueError if other is not a one digit integer
        '''
        if not isinstance(other, int):
            raise ValueError("Error - Can only divide with small integers.")
        r = 0
        new = Integer(self.getBase(), repr(self))
        for i in reversed(range(0, len(new))):
            r = new.getBase() * r + new[i]
            new[i] = r // other
            r = r % other
        new.clearIsb()
        return new

    def __mod__(self, other):
        '''
        Function to implement the division of an Integer with a one digit Integer
        :param other - the Divisor (the Dividend is self)
        :return an Integer representing the remainder of the division of self and other
        :raises ValueError if other is not a one digit integer
        '''
        if not isinstance(other, int):
            raise ValueError("Error - Modulo only defined on integers.")
        r = 0
        for i in reversed(range(0, len(self))):
            r = (r * self.getBase() + self[i]) % other
        return r

    def _compare(self, other):
        '''
        Comparator function for the Integer class.
        :param other: an Integer
        :return: 1 if self > other
                 0 if self == other
                -1 if self < other
        '''
        self.clearIsb()
        other.clearIsb()
        if len(self) > len(other):
            return 1
        elif len(self) < len(other):
            return -1
        else:
            for i in reversed(range(len(self))):
                if self[i] > other[i]:
                    return 1
                elif self[i] < other[i]:
                    return -1
            return 0

    def __eq__(self, other):
        '''
        == operator on self and other
        return the boolean value of the expression:
        self == other
        :param other: an Integer
        :return: True or False
        '''
        return self._compare(other) == 0

    def __lt__(self, other):
        '''
        < operator on self and other
        return the boolean value of the expression:
        self < other
        :param other: an Integer
        :return: True or False
        '''
        return self._compare(other) == -1

    def __le__(self, other):
        '''
        <= operator on self and other
        return the boolean value of the expression:
        self <= other
        :param other: an Integer
        :return: True or False
        '''
        return self._compare(other) <= 0

    def __gt__(self, other):
        '''
        > operator on self and other
        return the boolean value of the expression:
        self > other
        :param other: an Integer
        :return: True or False
        '''
        return self._compare(other) == 1

    def __ge__(self, other):
        '''
        >= operator on self and other
        return the boolean value of the expression:
        self >= other
        :param other: an Integer
        :return: True or False
        '''
        return self._compare(other) >= 0

    def substitutionMethod(self, destBase):
        '''
        Function to convert self in another base using the Substitution Method (recommended when the
            source base is less than the destination base)
        :param destBase: an integer from the set [2, 3, 4, 5, 6, 7, 8, 9, 10, 16] representing the base we want to
            convert our number
        :return: an Integer representing self in the destination base
        '''
        destNumber = Integer(destBase, "0")
        power = Integer(destBase, "1")
        for i in range(len(self)):
            destNumber = destNumber + power * Integer(destBase, Integer.Symbols[self[i]])
            power = power * Integer(destBase, Integer.Symbols[self._base])
        return destNumber

    def successiveDivison(self, destBase):
        '''
        Function to convert self in another base using the Successive Division Method (recommended when the
            source base is greater than the destination base)
        :param destBase: an integer from the set [2, 3, 4, 5, 6, 7, 8, 9, 10, 16] representing the base we want to
            convert our number
        :return: an Integer representing self in the destination base
        '''
        destNumber = Integer(destBase, "0")
        power = Integer(destBase, "1")
        aux = Integer(destBase, "10")
        copyOfSelf = deepcopy(self)
        while len(copyOfSelf) != 0:
            destNumber = destNumber + power * Integer(destBase, Integer.Symbols[copyOfSelf % destBase])
            copyOfSelf = copyOfSelf // destBase
            power = power * aux
        return destNumber

    def convertToBase(self, destBase):
        '''
        Function to decide which method from the following to choose:
            1. Rapid conversions - when one of the base is a power of the other one
            2. Substitution method - recommended when source base < destination base
            3. Successive Division method - recommended when source base > destination base
        :param destBase: an integer from the set [2, 3, 4, 5, 6, 7, 8, 9, 10, 16] representing the base we want to
            convert our number
        :return: an Integer representing self in the destination base
        '''
        if self._base <= destBase:
            return self.substitutionMethod(destBase)
        else:
            return self.succesiveDivisons(destBase)