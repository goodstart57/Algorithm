import sys
N = int(sys.stdin.readline().rstrip())
if N == 1:
    print(1)
else:
    i = 1
    while True:
        if N < 6 * i * (i+1) / 2 + 2:
            print(i+1)
            break
        i += 1