def nextFib(prev, cur):
	return prev + cur

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	prev = 1
	cur = 2
	sum = 0
	while cur < n:
		if cur % 2 == 0:
			sum += cur
		cur, prev = nextFib(prev, cur), cur
	print(sum)