def studyword(st):
    charlist = set(st)
    if len(charlist)==1:
        return st[0]

    countlist = sorted([(x, st.count(x)) for x in charlist], key=lambda tup: -tup[1])

    if countlist[0][1] == countlist[1][1]:
        return "?"
    else:
        return countlist[0][0]


print(studyword(input().upper()))