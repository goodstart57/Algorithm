N = int(input())  # 배달해야하는 설탕 무게

share: int = N // 5
remainder: int = N % 5

sugarDic = {0: 0, 1: 1, 2: 2, 3: 1, 4: 2}  # 나머지가 0,1,2,3,4인 경우 얼마나 5kg 빼고 3kg 더하는지

if N in [4, 7]:  # 4, 7kg인 경우 맞출 수 없다.
    print(-1)
else:
    print(share + sugarDic[remainder])




