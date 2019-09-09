T = int(input())

for i in range(T):
    RS = [x for x in input().split()]
    R, S = int(RS[0]), RS[1]
    result = []
    for char in S:
        for n in range(R):
            result.append(char)
    print("".join(result))