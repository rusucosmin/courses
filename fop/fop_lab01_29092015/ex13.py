def generateListForDebug():
	print("1 2", end=' ')
	for i in range(3, 50):
		cp = i
		div = 2
		while div*div <= cp:
			if cp % div == 0:
				print(div, end = ' ')
			while cp % div == 0:
				cp //= div
			div += 1
		if cp != 1:
			print (cp, end = ' ')
	print("\n")


n = int(input("give n, please "))
generateListForDebug()

i = 0
cnt = 1 #counting the first 1 from the array
div = 1
while cnt < n:
	i += 1
	div = 2
	ci = i
	while div * div <= ci:
		if ci % div == 0:
			cnt += 1
		while ci % div == 0:
			ci //= div
		if cnt == n:
			break
		div += 1
	if ci != 1:
		div = ci
		cnt += 1

print(div)
