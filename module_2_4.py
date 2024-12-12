numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i >= 2:
        flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            primes.append(i)
        else:
            not_primes.append(i)
print(primes, not_primes, sep = '\n')

