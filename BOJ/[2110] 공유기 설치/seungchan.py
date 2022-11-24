# 최대 가능한 거리는 1,000,000,000
# 너무 크다
# -> 이분 탐색

# 공유기 간의 거리를 가지고 이분 탐색을 하자

houses = []

N,C = map(int,input().split())

for i in range(N):
    houses.append(int(input()))

houses.sort()

# 공유기 간의 최단 거리 및 최대 거리
low = 1
high = houses[-1]-houses[0]

# 현재 계산한 거리로 공유기를 설치 했을때의 수를 가지고
# 이분 탐색 시행
while (low<=high):
    mid = (low+high)//2
    index = 0
    count = 1
    for i in range(len(houses)):
        if (houses[i]-houses[index])>=mid:
            index = i
            count += 1
    # 현재 계산한 거리로 공유기 설치시 가지고 있는 수보다 많이 설치했다면 길이를 늘려야함
    if count>=C:
        low = mid+1
    else:
        high = mid-1
print(high)

