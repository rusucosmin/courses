ans1 = []
ans2 = []

from copy import deepcopy

def back(p, st, n, m, length):
#	print(st)
	ans1.append(deepcopy(st))
	if p == length:
		return
	for i in range(n):
		st.append(i + 1)
		if abs(st[p - 1] - st[p]) >= m:
			back(p + 1, st, n, m, length)
		st.pop()
	
def getSolutionRecursive(n, m, length):
	for i in range(n):
		#st.append(i + 1)
		st = [i + 1]
		back(1, st, n, m, length)
		#st = st[:-1]

class Parameters:
	def __init__(self, p, ind, st):
		self.p = p
		self.ind = ind
		self.st = st
	
def backIterative(st, n, m, length):
	recStack = []
	recStack.append(Parameters(0, 0, st))
	while len(recStack):
		act = recStack.pop()
		if act.ind == 0:
			ans2.append(deepcopy(act.st))
#		print(act.st)
		if act.p == length - 1:
			continue
		for i in range(act.ind, n):
			if abs(act.st[act.p] - i - 1) >= m:
				new = Parameters(act.p + 1, 0, deepcopy(act.st))
				act.ind = i + 1
				new.st.append(i + 1)
				recStack.append(act)
				recStack.append(new)
				break

#yield, yield from

#specificatii

#teste

#refractoring
			
def getSolutionIterative(n, m, length):
	for i in range(n):
		st = [i + 1]
		backIterative(st, n, m, length)
	
n = int(input("n = "))
m = int(input("m = "))
length = int(input("length = "))

#getSolutionRecursive(n, m, length)
getSolutionIterative(n, m, length)

#assert(sorted(ans1) == sorted(ans2))
print(len(ans1))
print(ans1)
print(len(ans2))
print(ans2)

if len(ans2) == 0:
	print("There is no such array!")
else:
	print("Here are the solutions:")
	for list in ans2:
		print(list)


