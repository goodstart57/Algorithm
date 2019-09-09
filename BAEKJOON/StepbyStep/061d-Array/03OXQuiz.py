import sys


def summation(n):
    return sum(range(1, n + 1))


N = int(sys.stdin.readline().rstrip())
for i in range(N):
    print(sum(list(map(summation, map(len, filter(None, sys.stdin.readline().rstrip().split("X")))))))
