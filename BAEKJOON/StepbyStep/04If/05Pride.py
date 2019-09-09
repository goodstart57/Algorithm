import sys
C = int(sys.stdin.readline().rstrip())

for i in range(C):
    score = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
    mean = sum(score[1:], 0.0)/score[0]
    print("%.3f%%"%(len(list(filter(lambda x: x > mean, score[1:])))/score[0]*100), sep="")