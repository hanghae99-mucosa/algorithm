# https://grazinggoat.notion.site/9-27-6751af5a584542a69c155ca846bb74c4


# 시작점과 기준점을 주고 최단거리를 찾는다
# 각 경로의 비용은 동일하다
# -> BFS

from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

def bfs(n, m, maze):
    visited = [[0 for _ in range(m)]for _ in range(n)]

    # 시작위치 셋팅
    visited[0][0] = 1

    # 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # list.pop(0)의 time complexity O(N) -> deque사용-O(1)
    Q = deque([(0, 0)])

    while Q:
        x, y = Q.popleft()

        if x == n-1 and y == m-1:  # 목적지 도착
            return visited[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m: # 미로 내 영역인지 확인
                if maze[nx][ny] == 1 and visited[nx][ny] == 0:  # 방문하지 않은곳
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx, ny))

print(bfs(n,m,maze))