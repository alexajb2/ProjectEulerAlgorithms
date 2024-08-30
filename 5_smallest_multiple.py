import math 
from functools import reduce # applies a function of two areguments cumulatively on an iterable

def lcm(a, b): 
	return abs(a*b) // math.gcd(a, b)

def lcm_of_range(n): 
	return reduce(lcm, range(1, n+1))

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	result = lcm_of_range(n)
	print(result)


# input = 3
# lcm_of_range(3)
# reduce(lcm, range(1, 4))
# reduce(lcm, [1, 2, 3])
# lcm(1, 2) = 2 // 1 = 2
# lcm(lcm(1, 2), 3) = 6 // 1 = 6

# input = 4
# lcm_of_range(5)
# reduce(lcm, range(2, 5))
# reduce(lcm, [1, 2, 3, 4])
# lcm(1, 2) = 2 // 1 = 2
# lcm(lcm(1, 2), 3) = 6 // 1 = 6
# lcm(lcm(lcm(1, 2), 3), 4) = 24 // 2 = 12