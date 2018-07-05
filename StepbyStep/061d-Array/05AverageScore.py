import sys

scorelist = []
for i in range(5):
    score = int(sys.stdin.readline().rstrip())
    if score < 40: score = 40
    scorelist.append(score)

print(int(sum(scorelist)/len(scorelist)))

