import sys
(lambda f: print('\n'.join(','.join(str(m) for m in sorted(list(set(int(n) for n in line.strip().split(','))))) for line in f)))(open(sys.argv[1], 'r'))
