t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n -= 1
    threes = n // 3
    fives = n // 5
    fifteens = n // 15 # double counted
    print((3*threes*(threes+1) + 5*fives*(fives+1) - 15*fifteens*(fifteens+1))//2)