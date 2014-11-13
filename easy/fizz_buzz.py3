import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        nums = line.split(' ')
        a, b, n = (int(x) for x in [nums[0], nums[1], nums[2]])
        for i in range(1, n + 1):
            if i % a == 0 or i % b == 0:
                if i % a == 0:
                    print('F', end='')
                if i % b == 0:
                    print('B', end='')
            else:
                print('%d' % i, end='')

            print('', end=('\n' if i == n else ' '))
