# 출발지와 목적지가 주어지고 최소 이동거리를 통해 이동
# -> bfs

# 기존의 bfs는 상하좌우의 이동 케이스가 있지만
# 체스의 나이트는 현위치에서 이동할 수 있는 케이스가 8개가 있음
# 이동할 수 있는 케이스를 배열에 담아 두고
# 큐에서 꺼낸 위치에 대하여 bfs 시행
from collections import deque

N = int(input())

moves = [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]

def bfs(size,x,y,fx,fy):
    visited = [[0 for _ in range(size)]for _ in range(size)]

    Q = deque([(x,y)])

    while Q:
        x, y = Q.popleft()

        if x == fx and y == fy:  # 목적지 도착
            return visited[x][y]
        
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            
            if 0 <= nx < size and 0 <= ny < size: # 미로 내 영역인지 확인
                if visited[nx][ny] == 0:  # 방문하지 않은곳
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx, ny))

for _ in range(N):
    size = int(input())
    x, y = map(int,input().split())
    fx, fy = map(int,input().split())

    print(bfs(size, x,y,fx,fy))