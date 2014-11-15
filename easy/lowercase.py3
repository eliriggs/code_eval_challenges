import sys
(lambda f: print('\n'.join(line.strip().lower() for line in f)))(open(sys.argv[1], 'r'))
