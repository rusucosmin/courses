'''
Display in all possible modalities the numbers from 1 to n, such that between any two
numbers on consecutive positions, the difference in absolute value is at least m.
'''

def back(step, stack, n, m, length):
    '''
        RECURSIVE SOLUTION
        Display in all possible modalities the numbers from 1 to
        n, such that between any two numbers on consecutive positions, the difference in absolute value is at
        least m.
        :param step: the number of numbers already chosen
        :param stack: this is where i store my numbers
        :param n: the range of number (see task)
        :param m: the minimum delta (see task)
        :param length: the maximum length of a sequence (see task)
    '''
    yield stack
    if step == length:
        return
    for i in range(n):
        if abs(stack[step - 1] - i - 1) >= m:
            yield from back(step + 1, stack + [i + 1], n, m, length)

def getSolutionRecursive(n, m, length):
    '''
        RECURSIVE SOLUTION
        Auxiliary function to select the first item of the list and to call the back() function
        :param n: see task
        :param m: see task
        :param length: see task
    '''
    for i in range(n):
        yield from back(1, [i + 1], n, m, length)

class Parameters:
    '''
        Class to encapsulate all the data to simulate the recursive stack
        self.step = the step in the backtracking algorithm
        self.ind = the last index i was at the current step
        sef.stack = the chosen numbers so far
    '''
    def __init__(self, step, ind, stack):
        self.step = step
        self.ind = ind
        self.stack = stack

def backIterative(stack, n, m, length):
    '''
        Display in all possible modalities the numbers from 1 to
        n, such that between any two numbers on consecutive positions, the difference in absolute value is at
        least m.
        :param step: the number of numbers already chosen
        :param stack: this is where i store my numbers
        :param n: the range of number (see task)
        :param m: the minimum delta (see task)
        :param length: the maximum length of a sequence (see task)
    '''
    recStack = []
    recStack.append(Parameters(0, 0, stack))
    while len(recStack):
        stackTop = recStack.pop()
        if stackTop.ind == 0:
            yield stackTop.stack
#			print(act.st)
        if stackTop.step == length - 1:
            continue
        for i in range(stackTop.ind, n):
            if abs(stackTop.stack[stackTop.step] - i - 1) >= m:
                new = Parameters(stackTop.step + 1, 0, stackTop.stack + [i + 1])
                stackTop.ind = i + 1
                recStack.append(stackTop)
                recStack.append(new)
                break


def getSolutionIterative(n, m, length):
    '''
        ITERATIVE METHOD
        :param n: from the task
        :param m: from the task
        :param length: from the task
    '''
    for i in range(n):
        yield from backIterative([i+1], n, m, length)

def testRecIter(n, m, length):
    '''
        Test function to check if the recursive and iterative solution gives the same result.
        :param n:
        :param m:
        :param lenght:
    '''
    recursive = []
    iterative = []
    for x in getSolutionRecursive(n, m, length):
        recursive.append(x)
    for y in getSolutionIterative(n, m, length):
        iterative.append(y)
    assert recursive == iterative
    return recursive


def testEquals(n, m, length, solution):
    '''
        Function to check a test case for  our task
        :param solution: the solution to the (n, m, length) test case
        :raises: AssertionError if the recursive method is different that the iterative one, or if
                                they are not the same as the array solution
    '''
    result = testRecIter(n, m, length)
    assert result == solution

def test():
    '''
        Main test functon to call the auxiliary test function
    '''
    testEquals(5, 3, 2, [[1], [1, 4], [1, 5], [2], [2, 5], [3], [4], [4, 1], [5], [5, 1], [5, 2]])
    testEquals(5, 2, 2, [[1], [1, 3], [1, 4], [1, 5], [2], [2, 4], [2, 5], [3], [3, 1], [3, 5], [4], [4, 1], [4, 2], [5], [5, 1], [5, 2], [5, 3]])


def main():
    '''
        Main function
    '''
    try:
        n = int(input("n = "))
        m = int(input("m = "))
        length = int(input("length = "))
    except ValueError:
        print("Values should be integers!")

    print("Recursive")
    for x in getSolutionRecursive(n, m, length):
        print(x)
    print("Iterative")
    for y in getSolutionIterative(n, m, length):
        print(y)

if __name__ == '__main__':
    test()
    main()

