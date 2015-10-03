contains = True;

while contains:														#while the string still contains other characters than digits
	contains = False;
	a = input("please insert the number " )		#get the number as a string
	for x in a:
		if not x in "0123456789":
			contains = True
		
fr = [0 for i in range(0, 10)]
for x in a:
	fr[ord(x) - ord('0')] += 1

for x in range(1, 10):
	if fr[x] != 0:
		first = x
		break

fr[first] -= 1

print(first, end='')
for x in range(0, 10):
	for i in range(0, fr[x]):
		print(x, end='')
