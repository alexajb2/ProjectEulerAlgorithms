import math

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())

	n_sum = n*(n+1)//2
	square_of_sum = int(math.pow(n_sum, 2))

	sum_of_squares = 0
	for i in range(1, n+1):
		sum_of_squares += math.pow(i, 2)
	sum_of_squares = int(sum_of_squares)

	print(square_of_sum-sum_of_squares)