# 점화식을 생각해보자
# 조건이 다양하게 많았는데 쉽게 보면
# i번째에는 i-1번째에 칠한 색을 제외하고 칠 할수 있음
# 미리 i번째에 특정 색을 칠했다고 생각하는게 아니라 i번째의 모든 색깔 케이스에 대해서 비용을 계산해야함
N = int(input())
houses=[list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    houses[i][0] += min(houses[i-1][1],houses[i-1][2])
    houses[i][1] += min(houses[i-1][0],houses[i-1][2])
    houses[i][2] += min(houses[i-1][0],houses[i-1][1])

print(min(houses[-1]))