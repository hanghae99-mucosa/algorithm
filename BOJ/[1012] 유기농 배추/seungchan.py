# https://grazinggoat.notion.site/9-29-44cd8db520ff4508ae2818b2536ea923

# 각 위치가 주어지고 갈수 있는 곳을 모두 가보고자 함
# -> DFS

# 주어진 배추의 위치를 하나씩 받아서 DFS 탐색을 하고 갔던곳은 체크
# 주어진 배추의 위치에 대해서 dfs를 정상적으로 했다면 count+=1

# 백준에서는 재귀의 깊이를 제한
# 아래와 같이 재귀의 깊이를 커스텀
import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())

def dfs(x,y):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            #아직 방문하지 않았고 영역 이내인 경우
            if 0 <= nx < N and 0 <= ny < M and land[nx][ny] == 1:
                # 방문했음을 표시
                land[nx][ny] = 0
                dfs(nx,ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = [list(map(int, input().split())) for _ in range(K)]

    count =0

    # 땅 초기화
    land = [[0 for _ in range(M)]for _ in range(N)]

    # 땅에 배추위치 표시
    for cabbage in cabbages:
        land[cabbage[1]][cabbage[0]] = 1
    
    for cabbage in cabbages:
        # 아직 방문하지 않은 배추 땅일 경우
        if land[cabbage[1]][cabbage[0]] == 1:
            count+=1
            dfs(cabbage[1],cabbage[0])

    print(count)
