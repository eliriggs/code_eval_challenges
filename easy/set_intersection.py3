import sys
(lambda f: print('\n'.join( ','.join(str(n) for n in sorted(list(set(line.strip().split(";")[0].split(",")) & set(line.strip().split(";")[1].split(","))))) for line in f if not line.strip() == "")))(open(sys.argv[1], 'r'))
