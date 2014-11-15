import sys
with open(sys.argv[1], 'r') as f:
    for line in f:
        total = 0
        for char in line.strip():
            total += int(char)
        print(str(total))
