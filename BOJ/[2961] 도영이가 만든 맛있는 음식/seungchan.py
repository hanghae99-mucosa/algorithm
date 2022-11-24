import sys
N = int(input())

material = [list(map(int, input().split())) for _ in range(N)]
minDiff = sys.maxsize

for i in range(1,1<<N):
    count = 0
    sour = 1
    bitter = 0
    while i:
        if i%2 == 1:
            sour*=material[count][0]
            bitter+=material[count][1]
        count+=1
        i//=2
    if abs(sour-bitter) < minDiff:
        minDiff = abs(sour-bitter)

print(minDiff)
