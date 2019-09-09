import sys
N = int(sys.stdin.readline().rstrip())


def hansoo(N):
    if N < 100:
        return N
    else:
        count = 99
        for i in range(100, N+1):
            li = [int(x) for x in str(i)]
            li2 = [li[a] - li[a+1] for a in range(len(li)-1)]
            if li2[0] == li2[1]:
                count += 1
        return count


print(hansoo(N))