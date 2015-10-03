#so i created two functions
#palindrome(n) : it returns the reversed string

#however, if we are not allowed to use the number as a string, we should use the second function, palindrome_int

def palindrome(n):
	return n[::-1]

def palindrome_int(n):
	m = 0
	while n > 0:
		m = m * 10 + n % 10
		n //= 10
	return m	

a = input("Insert n ")
print (palindrome_int(int(a)))
