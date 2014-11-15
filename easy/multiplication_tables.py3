n = 12

print('\n'.join(''.join("{0:>4}".format(i * j) for j in range(1, n+1)).strip() for i in range(1, n+1)))
