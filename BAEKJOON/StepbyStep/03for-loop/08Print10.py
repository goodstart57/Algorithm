# 한 줄짜리 문자열을 입력받아서 10글자씩 출력하는 프로그램
istr = input()  # input()
strShare = len(istr) // 10
lastStrStart = strShare*10
lastStrEnd = lastStrStart + len(istr) % 10

for i in range(strShare):
    print(istr[i*10:i*10 + 10])
print(istr[lastStrStart:lastStrEnd + 1])


# 리스트로 변환해서 해결
# st = list(input())
# lind = len(st) // 10
# for i in range(lind):
#     print("".join(st[0:10]))
#     st = st[11:len(st)]
# print("".join(st))


