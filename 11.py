numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    d = 2
    while i % d != 0:
        d += 1
        if i == 1 or i == 2:
            break
    if i == d:
        primes.append(i)
    else:
        if i == 1:
            continue
        not_primes.append(i)
print(not_primes, primes)





