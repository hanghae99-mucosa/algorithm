N, K = map(int, input().split())
originalN = N
while True:
    testN = N
    rest = 0
    while testN:
        rest += testN % 2
        testN = testN//2
    if rest <= K:
        break
    else:
        N+=1

print(N-originalN)