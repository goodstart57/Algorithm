print(max(list(map(lambda x: int("".join(list(reversed(x)))), [x for x in input().split()]))))
