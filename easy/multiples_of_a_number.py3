import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        x, n = (int(i) for i in line.strip().split(','))
        m = 1
        while True:
            if n * m >= x:
                print(str(n * m))
                break
            else:
                m += 1
