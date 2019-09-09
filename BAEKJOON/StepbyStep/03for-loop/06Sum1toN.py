N = int(input())

share = N//2
result = (N + 1) * share
if N % 2 == 1:
    result += share + 1

print(result)