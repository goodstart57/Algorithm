'''
input() 대신에 sys.stdin.readline 사용
sys.stdin.readline은 개행문자까지 포함하기 때문에 rstrip 메소드 사용해야한다.
'''
import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    inp = [int(x) for x in sys.stdin.readline().rstrip().split(" ")]
    print(inp[0] + inp[1])