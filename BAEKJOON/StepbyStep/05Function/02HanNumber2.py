import sys

print(sum([i//100 + i%10 == i//10%10 * 2 or i<100 for i in range(1, int(sys.stdin.readline().rstrip())+1)]))