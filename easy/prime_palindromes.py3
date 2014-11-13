from math import sqrt

for i in range(1000, 1, -1):
    # if palindrome
    if str(i) == ''.join(reversed(str(i))):
        # if prime
        prime = True
        for j in range(2, i - 1):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(str(i))
            break
