import sys
N = int(sys.stdin.readline().rstrip())
i = 1
if N == 1:
    print("1/1")
else:
    while i <= N:
        N, i = N - i, i + 1
        if N <= i:
            if i % 2 == 0:
                N = i - N
                print(i-N, "/", 1+N, sep="")
            else:
                print(i-N+1, "/", N, sep="")
            break