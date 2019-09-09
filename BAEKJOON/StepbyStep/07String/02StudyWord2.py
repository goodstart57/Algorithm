from collections import Counter
n = Counter(input().upper()).most_common()
print(n[0][0]) if len(n) == 1 or n[0][1] != n[1][1] else print('?')