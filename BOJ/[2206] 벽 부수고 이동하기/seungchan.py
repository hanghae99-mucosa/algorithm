# https://grazinggoat.notion.site/9-28-8f6f02ef76054bcc9cce6aff66cb0e60

# 시작점과 기준점을 주고 최단거리를 찾는다
# 각 경로의 비용은 동일하다
# -> BFS

from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

def bfsWithBreak(n, m, maze):
    # 벽을 부순 경우와 부수지 않고 간 경우 모두 기록 하기위해 n*m*2
    visited = [[[0]*2 for _ in range(m)]for _ in range(n)]

    visited[0][0][0] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # x좌표, y좌표, 벽 부순 여부
    Q = deque([(0, 0, 0)])

    while Q:
        x, y, isBroken = Q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][isBroken]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # 갈수 있는 곳
                if maze[nx][ny] == 0 and visited[nx][ny][isBroken] == 0:
                    visited[nx][ny][isBroken] = visited[x][y][isBroken] + 1
                    Q.append((nx, ny, isBroken))

                # 갈수 없지만 벽을 부술수 있는 상태
                elif maze[nx][ny] == 1 and isBroken == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    Q.append((nx, ny, 1))
    return -1

print(bfsWithBreak(n,m,maze))