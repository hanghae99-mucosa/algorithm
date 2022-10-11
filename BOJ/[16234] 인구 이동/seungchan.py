# 하나의 국가에서 인접해있는 가까운 국가와 인구차이를 비교
# -> BFS

# 땅을 하나씩 방문하면서 아직 방문하지 않았던 곳이라면 BFS 시행
# BFS 시행시 인접 국가부터 방문하면서 인구차이를 비교
# (이때도 방문한 국가 표시해줌)

# pypy로 제출해서 실행속도를 높여서 통과
# (pypy는 자주쓰는 코드를 캐싱해둠)

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, L, R = map(int, input().split())
domain = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(N)]for _ in range(N)]

day = 0

def bfs(i,j):
    visited[i][j] = 1
    near = [[i,j]]
    population = domain[i][j]

    Q = deque([(i,j)])

    while Q:
        x, y = Q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N: # 미로 내 영역인지 확인
                diff = abs(domain[x][y]-domain[nx][ny])
                if diff<=R and diff>= L and visited[nx][ny] == 0:  # 방문하지 않은곳
                    visited[nx][ny] = visited[x][y] + 1

                    # 연합에 추가
                    near.append([nx,ny])
                    
                    # 인구수 종합
                    population+=domain[nx][ny]

                    Q.append((nx, ny))
    
    avg = int(population/len(near))

    for country in near:
        domain[country[0]][country[1]] = avg

    # 인구이동이 일어나지 않은 경우
    if avg == population:
        return 0
    # 인구이동이 일어난 경우
    else:
        return 1

while True:
    # 인구이동이 일어났는지 여부 체크
    whileCheck = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                whileCheck += bfs(i,j)
    
    # 인구이동이 한번이라도 일어난 경우
    if whileCheck:
        day+=1
        visited = [[0 for _ in range(N)]for _ in range(N)]
    else:
        break

print(day)