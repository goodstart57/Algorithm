import sys
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

mult = str(A*B*C)

for i in range(10):
    print(mult.count(str(i)))