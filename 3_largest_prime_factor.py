t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    d = 2
    max_prime = 1
    while n > 1:
        while n % d == 0:
            max_prime = d
            n //= d
        d = d + 1
        if d*d > n:
            if n > d:
                max_prime = n
            break
    print(max_prime)