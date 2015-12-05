from copy import deepcopy

__author__ = 'cosmin'

from exception.integerexception import IntegerException


class Integer:
    '''
    Class to represent a number

    self._length: the number of digits of the number
    self._digits
    self._base : the base of the number
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

    def valueOf(number_repr):
        if number_repr in Integer.Values.keys():
            return Integer.Values[number_repr]
        raise ValueError("Not a digit...")

    def __init__(self, base, number_repr):
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

    def append(self, value):
        self._digits.append(value);
        self._length += 1

    def __repr__(self):
        self.clearIsb()
        number_repr = ""
        for digit in self._digits[::-1]:
            number_repr += Integer.Symbols[digit]
        if number_repr == "":
            number_repr = "0"
        return number_repr

    def __str__(self):
        return repr(self) + " (" + str(self._base) + ")"

    def clearIsb(self):
        while len(self) > 0 and self[-1] == 0:
            self._digits.pop()
            self._length -= 1

    def __getitem__(self, item):
        return self._digits[item]

    def __setitem__(self, key, value):
        self._digits[key] = value

    def __len__(self):
        return self._length

    def append(self, val):
        self._length += 1
        self._digits.append(val)

    def getLength(self):
        return self._length

    def getBase(self):
        return self._base

    def __add__(self, other):
        '''
        void Add(Huge A, Huge B)
        /* A <- A+B */
        { int i,T=0;

          if (B[0]>A[0])
            { for (i=A[0]+1;i<=B[0];) A[i++]=0;
              A[0]=B[0];
            }
            else for (i=B[0]+1;i<=A[0];) B[i++]=0;
          for (i=1;i<=A[0];i++)
            { A[i]+=B[i]+T;
              T=A[i]/10;
              A[i]%=10;
            }
          if (T) A[++A[0]]=T;
        }
        '''
        if not isinstance(other, Integer):
            raise ValueError("Error - Addition on two different objects.")
        if self._base != other._base:
            raise ValueError("Error - Addition on two Integgers with different bases.")
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
        void Subtract(Huge A, Huge B)
            /* A <- A-B */
            { int i, T=0;

              for (i=B[0]+1;i<=A[0];) B[i++]=0;
              for (i=1;i<=A[0];i++)
                A[i]+= (T=(A[i]-=B[i]+T)<0) ? 10 : 0;
                /* Adica A[i]=A[i]-(B[i]+T);
                   if (A[i]<0) T=1; else T=0;
                   if (T) A[i]+=10; */
              while (!A[A[0]]) A[0]--;
            }
        :param other:
        :return:
        '''
        if not isinstance(other, Integer):
            raise ValueError("Error - Subtraction on two different objects.")
        if self.getBase() != other.getBase():
            raise ValueError("Error - Subtraction on two words with different bases.")
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
      void MultHuge(Huge A, Huge B, Huge C)
            /* C <- A x B */
            { int i,j,T=0;

              C[0]=A[0]+B[0]-1;
              for (i=1;i<=A[0]+B[0];) C[i++]=0;
              for (i=1;i<=A[0];i++)
                for (j=1;j<=B[0];j++)
                  C[i+j-1]+=A[i]*B[j];
              for (i=1;i<=C[0];i++)
                { T=(C[i]+=T)/10;
                  C[i]%=10;
                }
              if (T) C[++C[0]]=T;
            }
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
        unsigned long Divide(Huge A, unsigned long X)
            /* A <- A/X si intoarce A%X */
            { int i;
              unsigned long R=0;

              for (i=A[0];i;i--)
                { A[i]=(R=10*R+A[i])/X;
                  R%=X;
                }
              while (!A[A[0]] && A[0]>1) A[0]--;
              return R;
            }
            :param other:
            :return:
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
        unsigned long Mod(Huge A, unsigned long X)
            /* Intoarce A%X */
            { int i;
              unsigned long R=0;

              for (i=A[0];i;i--)
                R=(10*R+A[i])%X;
              return R;
            }
        :param other:
        :return:
        '''
        if not isinstance(other, int):
            raise ValueError("Error - Modulo only defined on integers.")
        r = 0
        for i in reversed(range(0, len(self))):
            r = (r * self.getBase() + self[i]) % other
        return r

    def _compare(self, other):
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
        return self._compare(other) == 0

    def __lt__(self, other):
        return self._compare(other) == -1

    def __le__(self, other):
        return self._compare(other) <= 0

    def __gt__(self, other):
        return self._compare(other) == 1

    def __ge__(self, other):
        return self._compare(other) >= 0

    def substitutionMethod(self, destBase):
        destNumber = Integer(destBase, "0")
        power = Integer(destBase, "1")
        for i in range(len(self)):
            destNumber = destNumber + power * Integer(destBase, Integer.Symbols[self[i]])
            power = power * Integer(destBase, Integer.Symbols[self._base])
        return destNumber

    def succesiveDivisons(self, destBase):
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
        if self._base <= destBase:
            return self.substitutionMethod(destBase)
        else:
            return self.succesiveDivisons(destBase)


