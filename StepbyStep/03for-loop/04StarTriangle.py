N = int(input())

for i in range(1, N+1):
    print("*"*i)

for i in range(1, N+1):
    print(" "*(N-i), "*"*i, sep="")

for i in range(N, 0, -1):
    print("*"*i)

for i in range(N, 0, -1):
    print(" "*(N-i), "*"*i, sep="")
