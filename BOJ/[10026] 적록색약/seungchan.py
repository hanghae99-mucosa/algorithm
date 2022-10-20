# 영역 구분을 하는 문제
# 어떤 기준에서 갈수 있는 모든 곳을 가봐야한다.
# -> DFS

# 적록색약인 경우와 그렇지 않은 경우로 나누어서 진행
# 적록색약인 경우와 아닌 경우 각각의 visited를 생성

# 그림의 좌표마다 방문하지 않은 경우라면 dfs 시행
# 한번의 dfs 시행은 하나의 구분된 영역을 의미(count 해줌)

import sys
sys.setrecursionlimit(100000)

N = int(input())
picture = [list(input()) for _ in range(N)]
# visited[0]는 적록색약, visited[1]은 적록색약이 아닌 경우
visited = [[[0 for _ in range(N)]for _ in range(N)] for _ in range(2)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 적록색약인 경우, 아닌 경우 섹션 수
section = [0,0]

def dfs(x,y,visible):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            # 적록색약인 경우
            if visible:
                if visited[0][nx][ny]==0 and picture[nx][ny]==picture[x][y]:
                    visited[0][nx][ny] = 1
                    dfs(nx,ny,visible)
            else:
                color = set(picture[x][y])
                if "B" not in color:
                    color.add("R")
                    color.add("G")
                
                if visited[1][nx][ny]==0 and picture[nx][ny] in color:
                    visited[1][nx][ny] = 1
                    dfs(nx,ny,visible)

for x in range(N):
    for y in range(N):
        if visited[0][x][y] == 0:
            visited[0][x][y] = 1
            dfs(x,y,True)
            section[0]+=1
        if visited[1][x][y] == 0:
            visited[1][x][y] = 1
            dfs(x,y,False)
            section[1]+=1

for s in section:
    print(s,end=" ")