# 한 지점에서 갈수 있는 모든 영역을 탐색해야한다
# -> DFS

# 주어진 input에서 최저 높이와 최고 높이를 찾음
# 비가 최저 높에서 최고 높이까지 오는 경우 각각에 대해서
# 분리 되는 영역의 수를 찾는다

# 분리되는 영역은 찾기
# 1. 주어진 지도에서 물에 잠기지 않았고 아직 방문하지 않았다면
# 2. 그곳에서 DFS 시행하면서 물에 잠기지 않은 곳을 DFS로 탐색을 하며 방문여부 체크
# 3. 한번의 DFS가 끝나면 그건 하나의 영역이므로 카운트

import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maxRain = 0
minRain = 101
maxAreaCount = 1

N = int(input())
areas =[]

visited = [[0 for _ in range(N)]for _ in range(N)]

for _ in range(N):
    area = list(map(int, input().split()))
    maxRain = max(max(area),maxRain)
    minRain = min(min(area),minRain)
    areas.append(area)

def dfs(x,y,rain):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 영역 이내, 내린 비보다 높이가 높고, 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < N and areas[nx][ny] > rain and visited[nx][ny]==0:
                visited[nx][ny] = 1
                dfs(nx,ny,rain)


for rain in range(minRain,maxRain):
    areaCount = 0
    for x in range(N):
        for y in range(N):
            if areas[x][y] > rain and visited[x][y]==0:
                dfs(x,y,rain)
                areaCount += 1
    visited = [[0 for _ in range(N)]for _ in range(N)]
    if maxAreaCount< areaCount:
        maxAreaCount = areaCount

print(maxAreaCount)
