N = int(input())
mycount = 0

def groupwordcheck(word):
    unqstr = list(set(word))
    for char1 in unqstr:
        if (word.count(char1)) != ((len(word) - list(reversed(word)).index(char1)) - word.index(char1)):
            return 0
    return 1


for i in range(N):
    mycount += groupwordcheck(input())

print(mycount)