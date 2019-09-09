import sys

sc = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(sc) - 1):
    sc[i] = sc[i+1] - sc[i]

if len(set(sc[:7])) != 1:
    print("mixed")
elif sc[0] == 1:
    print("ascending")
else:
    print("descending")