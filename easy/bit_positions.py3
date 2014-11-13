import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        n, p1, p2 = (int(i) for i in line.strip().split(','))
        print('true' if bin(n)[2:][::-1][p1-1] == bin(n)[2:][::-1][p2-1] else 'false')
