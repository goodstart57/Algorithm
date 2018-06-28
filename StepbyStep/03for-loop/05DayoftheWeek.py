xy = [int(x) for x in input().split(" ")]
x = xy[0]
y = xy[1]

DW = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT"}

diffDIC = {0: 0, 1: 1, 2: -1, 3: 0, 4: 0, 5: 1, 6: 1, 7: 2, 8: 3, 9: 3, 10: 4, 11: 4, 12: 5}

diff = (x-1)*30 + y + diffDIC[x-1]

print(DW[diff % 7])
