inp = [int(x) for x in input().split(" ")]

A, B, C = inp[0], inp[1], inp[2]

print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)
