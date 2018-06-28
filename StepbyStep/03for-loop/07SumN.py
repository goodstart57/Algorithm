N = int(input())
N_str = input()
result = 0

for i in range(len(N_str)):
    result += int(N_str[i])

print(result)