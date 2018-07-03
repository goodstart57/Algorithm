def find_snumbers(n, m):
    allnum = set(range(n, m))
    snum = {x + sum([int(a) for a in str(x)]) for x in range(n, m)}
    return allnum - snum


self_number = sorted(list(find_snumbers(1, 10001)))
for i in range(0, len(self_number)):
    print(self_number[i])