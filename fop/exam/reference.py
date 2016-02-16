def even_sum(l):
	if not isinstance(l, list):
		raise TypeError()
	sum = 0
	ok = False
	for x in l:
		if x % 2 == 1:
			sum = sum + x
			ok = True
	if not ok:
		raise ValueError()
	return sum

def test_even_sum():
	assert even_sum([-1, 1]) == 0
	assert even_sum([1, 2, 3]) == 4
	try:
		even_sum({'cosmin': 1, 'diana': 0})
		assert False
	except TypeError:
		pass

	try:
		assert even_sum([])
		assert False
	except ValueError:
		pass

def function(n):
	'''
		Function to test if the number n is prime or not
	'''
 	d = 2
  	while (d < n - 1) and n % d > 0:
   		d += 1
	return d >= n - 1

def getdp(n, l):
	dp = [0] * n
	for i in range(n): #iterez fiecare i (sfarsit de subsecventa)
		if l[i] % 2 == 0:
			for j in range(i):
				dp[i] = max(dp[i], dp[j] + 1)
	rasp = 0	
		
