inp = list(input())
grandic = dict(zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]))
for i in range(len(inp)):
    inp[i] = grandic[inp[i]] + 1
print(sum(inp))