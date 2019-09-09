alpha = input()
special_alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for cro in special_alphabet:
    alpha.replace(cro, "*")
print(len(alpha))