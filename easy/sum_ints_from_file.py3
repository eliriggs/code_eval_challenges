import sys
(lambda f: print(str(sum([int(line) for line in f]))))(open(sys.argv[1], 'r'))
