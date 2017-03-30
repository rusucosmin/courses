'''
8. The crossing river problemsolving techniques: BFS, GBFS
On one side of a river there are an adult, two children and a tiny little boat. The people
want to cross the river by boat. The tiny little boat can take either two children, either one child,
either one adult. Determine a sequence of moves to cross the river.

ACC -> binary representation
'''

import Queue

A = 3
B = 1
C = 2

class State:
    def __init__(self, conf):
        self._conf = conf

    def getState(self):
        return self._conf

    def move(self, arr):
        vals = [((self._conf & (1 << x)) > 0) for x in arr]
        uniq = set(vals)
        if len(uniq) != 1:
            return self
        else:
            now = State(self.getState())
            for x in arr:
                now._conf = now._conf ^ (1 << x)
            return now

    #BCCA
    def __eq__(self, other):
        return self.getState() == other.getState()

    def charFromPos(self, pos):
        if pos == 0:
            return "B"
        elif pos <= A:
            return "A"
        elif pos <= A + C:
            return "C"

    def __str__(self):
        binary = bin(self.getState())[2:].zfill(A + B + C)[::-1]
        left_side = [pos for pos in range(len(binary)) if binary[pos] == '0']
        right_side = [pos for pos in range(len(binary)) if binary[pos] == '1']
        left_str = ''.join([self.charFromPos(pos) for pos in left_side])
        right_str = ''.join([self.charFromPos(pos) for pos in right_side])
        return left_str.ljust(A + B + C + 10 - len(right_str)) + right_str

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self._conf

    def __cmp__(self, other):
        c1 = bin(self._conf).count('1')
        c2 = bin(other._conf).count('1')
        if c1 == c2:
            return 0
        elif c1 < c2:
            return -1
        else:
            return 1

class Problem:
    def __init__(self):
        self._initState = State(0)
        self._finalState = State((1 << (A + B + C)) - 1)

    def getInitialState():
        return self._initState

    def getFinalState():
        return self._finalState

    def expand(self, state):
        now = []
        #the bits are ordered like thos: 0 - boat, 1 .. A - adults, A + 1 .. A + C -> childs

        #move every adult first
        for i in range(0, A):
            now.append(state.move([0, i + 1]))

        #move every child
        for i in range(0, C):
            now.append(state.move([0, A + i + 1]))

        #move every pair of two children
        for i in range(0, C):
            for j in range(i + 1, C):
                now.append(state.move([0, A + i + 1, A + j + 1]))
        return now

    def heuristic(self, s1, s2):
        x1 = str(s1).count("1")
        x2 = str(s2).count("1")
        if x1 == x2:
            return 0
        elif x1 < x2:
            return -1
        else:
            return 1

class Controller:
    def __init__(self, problem):
        self._problem = problem

    def getProblem(self):
        return self._problem

    def orderStates(self, states):
        sortSt = sorted(states)
        return sortSt

    def findSol(self, now, dad):
        ans = [now]
        while now != self._problem._initState:
            now = dad[now]
            ans.insert(0, now)
        return ans

    def bfs(self, p):
        q = []
        vis = []
        dad = {}
        q.append(self._problem._initState)
        vis.append(self._problem._initState)
        while len(q) > 0:                           #while there are states in the queue
            now = q.pop(0)                          #get the first one
            if now == self._problem._finalState:
                return self.findSol(now, dad)
            for nxt in self._problem.expand(now):
                if nxt not in vis:
                    vis.append(nxt)
                    dad[nxt] = now
                    q.append(nxt)
        return []

    def gbfs(self, p):
        q = []
        vis = []
        dad = {}
        q.append(self._problem._initState)
        vis.append(self._problem._initState)
        while len(q) > 0:
            now = q.pop(0)
            if now == self._problem._finalState:
                return self.findSol(now, dad)
            for nxt in self.orderStates(self._problem.expand(now)):
                if nxt not in vis:
                    vis.append(nxt)
                    dad[nxt] = now
                    q.append(nxt)
        return []

class UI:
    def __init__(self, ctrl):
        self._ctrl = ctrl

    def printMainMenu(self):
        print("Currently having: " + str(B) + " boat " + str(A) + " adult(s) " + str(C) + " child(ren)\n")
        print("1. BFS")
        print("2. GBFS")
        print("3. Change the number of Adults: ")
        print("4. Change the number of Children: ")
        print("x. Exit")

    def run(self):
        global A, B, C
        while True:
            self.printMainMenu()
            op = raw_input("Input command: ")
            if op == "x":
                return
            elif op == "1":
                print("BFS: The road is: \n")
                path = self._ctrl.bfs(self)
                for x in path:
                    print(x)
                print("")
            elif op == "2":
                print("GBFS: The road is: \n")
                path = self._ctrl.gbfs(self)
                for x in path:
                    print(x)
                print("")
            elif op == "3":
                x = raw_input("A = ")
                try:
                    A = int(x)
                    if A < 0:
                        raise ValueError
                except ValueError as e:
                    print("Please insert a valid positive integer")
            elif op == "4":
                x = raw_input("C = ")
                try:
                    C = int(x)
                    if C < 0:
                        raise ValueError
                except ValueError as e:
                    print("Please insert a valid positive integer")
            else:
                print("Wrong command")

p = Problem()
ctrl = Controller(p)
ui = UI(ctrl)
ui.run()

