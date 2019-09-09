import sys
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

mult = A*B*C

countdict = dict(zip(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], [0]*10))

for i in str(mult):
    countdict[i] += 1

for i in range(10):
    print(countdict[str(i)])



'''
150
266
427
'''