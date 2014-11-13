i = 0
primes = 0
total = 0

while True:

    i += 1

    prime = True
    for j in range(2, i - 1):
        if i % j == 0:
            prime = False
            break

    if prime:
        primes += 1
        total += i

    if primes > 1000:
        break

total -= 1

print(str(total))
