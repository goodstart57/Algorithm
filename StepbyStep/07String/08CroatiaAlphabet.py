inp = input()
count = len(inp)
special_alphabet = ["c=", "c-", "d-", "lj", "nj", "s="]
for i in range(len(inp)-1):
    if inp[i:i+2] in special_alphabet:
        count -= 1
        continue
    elif inp[i:i+3] == "dz=":
        count -= 2
    elif i > 0:
        if inp[i:i+2] == "z=" and inp[i-1:i+2] != "dz=":
            count -= 1
print(count)