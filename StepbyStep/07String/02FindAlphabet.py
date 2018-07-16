word = input()
findlist = [-1] * 26

for f in word:
    findlist[ord(f) - 97] = word.find(f)

print(" ".join(list(map(str, findlist))))
# print(ord("a")) = 97

