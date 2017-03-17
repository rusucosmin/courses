'''
8. The crossing river problemsolving techniques: BFS, GBFS
On one side of a river there are an adult, two children and a tiny little boat. The people
want to cross the river by boat. The tiny little boat can take either two children, either one child,
either one adult. Determine a sequence of moves to cross the river.

ACC -> binary representation
'''

import Queue

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

    def flip(self, pos):
        now = State(self.getState())
        now._conf = now._conf ^ (1 << pos)
        return now
    #BCCA
    def __eq__(self, other):
        return self.getState() == other.getState()

    def __str__(self):
        return bin(self.getState())[2:].zfill(4)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self._conf

class Problem:
    def __init__(self):
        self._initState = State(0)
        self._finalState = State(15)

    def getInitialState():
        return self._initState

    def getFinalState():
        return self._finalState

    def expand(self, state):
        now = []
        now.append(state.move([0, 1]))
        now.append(state.move([0, 2]))
        now.append(state.move([0, 1, 2]))
        now.append(state.move([0, 3]))
        return now

    def heuristic(self, s1):
        x1 = str(s1).count("1")
        return x1
        x2 = str(s2).count("2")
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
        sortSt = sorted(states, key = lambda x: self._problem.heuristic(x))
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
        while len(q) > 0:
            now = q.pop(0)
            if now == self._problem._finalState:
                return self.findSol(now, dad)
            for nxt in self._problem.expand(now):
                if nxt not in vis:
                    vis.append(nxt)
                    dad[nxt] = now
                    q.append(nxt)
        return []

p = Problem()
ctrl = Controller(p)

print(ctrl.orderStates(ctrl.bfs(ctrl.getProblem())))



