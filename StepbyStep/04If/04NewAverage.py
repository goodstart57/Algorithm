import sys
N = int(sys.stdin.readline().rstrip())
score = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]

M = max(score)
score = list(map(lambda x: x / M * 100, score))
print(sum(score, 0.0)/N)