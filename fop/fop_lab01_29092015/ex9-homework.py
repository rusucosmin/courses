__author__  = 'cosmin'

def solveCase2(l):
	if l == [0]:
		return [0]
	# do a count sort
	fr = [0 for i in range(0, 10)]

	for x in l:
		fr[x] += 1

	for x in range(1, 10):
		if fr[x] != 0:
			first = x
			break
	fr[first] -= 1
	ret = []
	ret.append(first)
	for x in range(0, 10):
		for y in range (0, fr[x]):
			ret.append(x)
	return ret

def extractDigits(x):  #functions that returns a list containing the digits of a number
	digits = []
	if x == 0:
		return [0]
	while x > 0:
		digits.append(x % 10)
		x = x // 10
	return digits
	
def readInput():  # function that reads input and returns an integer or None if the user did not type a number
	try:
		ret = int(input("Please input a natural number "))
		if ret >= 0:
			return ret
		else: 
			print("You did not enter a valid number.")
			return None
	except:
		print("You did not enter a valid number.")
	return None

def solveCase1(digits): #function that returns the nondecreasing sorted list of list "digits"
	return sorted(digits)

def getInput():
	n = None
	while n is None:
		n = readInput()
	return n

def solve(n):
	#ambiguity in the problem statement
	digits = extractDigits(n)
	print ("Minimal number with beginning 0:")
	print (''.join(str(x) for x in solveCase1(digits)))
	print("Minimal number without beginnings 0:")
	print (''.join(str(x) for x in solveCase2(digits)))

if __name__ == '__main__':
	n = getInput()
	solve(n)
	
