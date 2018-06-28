NX = list(map(int, [x for x in input().split(" ")]))
A = list(map(str, filter(lambda x: x < NX[1], map(int, [x for x in input().split(" ")]))))
print(" ".join(A))

# start_time2 = time.time()
# NX = [int(x) for x in "10 5".split(" ")]
# A = [int(x) for x in "1 10 4 9 2 3 8 5 7 6".split(" ")]
# print(NX)
# print(A)
# print("--- %s seconds ---" %(time.time() - start_time2))

