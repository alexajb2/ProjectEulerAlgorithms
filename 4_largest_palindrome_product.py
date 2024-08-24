t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	palindrome = 0
	while palindrome==0:
		n -=1
		if str(n)==str(n)[::-1]:
			for j in range(100, 1000):
				if n % j == 0:
					f = n/j
					if f <= 999:
						palindrome=n
						break

	print(palindrome)