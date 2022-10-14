# N이 최대 15로 매우 작음
# -> 전부 탐색

# 1부터 N개까지 조합을 뽑으면서
# 뽑은 조합으로 최저 영양소 기준을 만족하면
# 이전에 계산한 최소비용과 비교해서 조합을 업데이트

from itertools import combinations

N = int(input())
foods = [list(map(int,input().split())) for _ in range(N+1)]
# 조합을 만들기 위한 N개의 숫자 배열
number = [i for i in range(1,N+1)]
# 최소 비용
minCost = float('inf')
# 최소 비용시의 조합
minCostFood = []

# 1에서부터 N개까지 뽑는 조합
for i in range(1,N+1):
    # 해당 조합에서 나온 재료
    for nums in combinations(number,i):
        candidate = [0,0,0,0,0]
        for num in nums:
            candidate[0] += foods[num][0]
            candidate[1] += foods[num][1]
            candidate[2] += foods[num][2]
            candidate[3] += foods[num][3]
            candidate[4] += foods[num][4]
        # 영양분이 일정 이상되고 이전에 게산한 최소비용보다 작거나 작은 경우
        if candidate[0]>=foods[0][0] and candidate[1]>=foods[0][1] and candidate[2]>=foods[0][2] and candidate[3]>=foods[0][3] and candidate[4]<=minCost:
            nums = list(nums)
            # 최소비용이 같은 경우
            if candidate[4]==minCost:
                # 사전 순으로 빠른 경우
                if nums < minCostFood:
                    minCost = candidate[4]
                    minCostFood = nums
            else:
                minCost = candidate[4]
                minCostFood = nums

# 조건을 만족하는 답이 없는 경우
if len(minCostFood)==0:
    print(-1)
else:
    print(minCost)
    for food in minCostFood:
        print(food,end=' ')