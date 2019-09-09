'''
시험 점수를 입력받아 90 ~ 100점은 A,
80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''

# import sys
# score = int(sys.stdin.readline().rstrip())
#
# if score > 100 | score < 0:
#     print("시험 점수를 바르게 입력해주세요")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# 아스키 코드 사용
import sys
score = int(sys.stdin.readline().rstrip()) // 10

if score == 10:
    print("A")
elif score < 6:
    print("F")
else:
    print(chr(65 + (9 - score)))


