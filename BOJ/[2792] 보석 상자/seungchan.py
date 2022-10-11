# 각 색깔별 정보를 배열에 두고 최댓값을 2로 나누면서
# 다시 배열에 넣어 길이가 N이 될때까지 시행헀을때
# 배열의 최댓값을 프린트
# -> heapq를 사용함에도 시간초과

###### 첫번째 풀이 ######
import heapq

N, M = map(int, input().split())

hp = []

for _ in range(M):
    num = int(input())
    heapq.heappush(hp,(-num,num))

while len(hp)!=N:
    color = heapq.heappop(hp)
    color = color[1]
    if color!=0:
        sub1 = round(color/2)
        sub2 = int(color/2)
        heapq.heappush(hp,(-sub1,sub1))
        heapq.heappush(hp,(-sub2,sub2))

print(heapq.heappop(hp)[1])

###### 두번째 풀이 ######

N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]

left = 1
right = max(colors)

while left <= right:
    mid = (left+right) // 2
    total = 0
    for color in colors:
        if color % mid == 0:
            total += color//mid
        else:
            total += (color//mid) + 1
    # total이 더 크다는 것은
    # N명보다 더 많은 사람이 보석을 가져간 것
    # 그렇기 때문에 더 적게 가져가도록 하기위해 left를 증가시켜야함
    # 한 명이 가져가는 보석의 수를 늘림
    if total > N:
        left = mid + 1

    else:
        right = mid - 1

print(left)