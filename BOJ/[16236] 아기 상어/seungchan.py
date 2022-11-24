# 상어는 기본적으로 자신과 가장 가까운 물고기중 자신보다 작은 물고기를 먹는다.
# 기본적으로 bfs 적용
# bfs를 통해 최초 발견한 먹을수 있는 물고기의 위치를 저장
# 이후 위에서 발견한 물고기보다 먼거리에 있는 곳은 큐에서 바로 제거
# 만약 같은 거리의 먹을수 있는 물고기가 또 발견이 된다면 더 위쪽, 더 왼쪽인 경우에 업데이트(bfs임으로 더 거리가 짧은 경우는 나타나지 않음)
# bfs 종료시 얻게된 물고기 위치로 상어를 이동시켜 먹고
# 해당 물고기를 지우고 먹은 횟수 카운트를 증가시켜 먹은 횟수가 현재 상어 사이즈와 같다면 사이즈를 증가시키고 먹은 횟수 초기화

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())

sizeOfShark = 2
eatCount = 0
space = []
time = 0
shark = []
fish = []

for i in range(N):
    row = list(map(int,input().split()) )
    for j in range(N):
        if row[j] == 9:
            shark = [i,j]
            row[j] = 0  # 시작 위치도 지나갈수 있게 해줌
    space.append(row)

def bfs(x,y):
    visited = [[0 for _ in range(N)]for _ in range(N)]
    Q = deque([(x, y)])

    # 거리,x좌표,y좌표
    fish = []

    while Q:
        x, y = Q.popleft()
        
        # 현재 먹을수 있는 물고기보다 거리가 먼곳이라면 더 이상 탐색 불필요
        if len(fish) != 0:
            if fish[0] < visited[x][y]:
                continue
        
        # 먹을수 있는 물고기인 경우
        if 0< space[x][y] < sizeOfShark:
            if len(fish) == 0:
                fish = [visited[x][y],x,y]
            # 기존에 먹을수 있는 물고기랑 거리가 같지만 더 위쪽이고 더 왼쪽인 경우
            else:
                if fish[1]>x:
                    fish = [visited[x][y],x,y]
                elif fish[1]==x:
                    if fish[2] > y:
                        fish = [visited[x][y],x,y]
            # 현재 찾은 물고기보다 거리가 더 먼곳은 탐색 불필요하기 때문에 패스
            continue


        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N:
                if space[nx][ny] <= sizeOfShark and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append((nx, ny))
    # 거리,x좌표,y좌표
    return fish

while True:
    fish = bfs(shark[0],shark[1])

    if len(fish) == 0:
        print(time)
        break
    else:
        time += fish[0]
        shark[0]=fish[1]
        shark[1]=fish[2]

        # 먹은 물고기 제거
        space[shark[0]][shark[1]] = 0

        #먹은횟수 증가 -> 먹은 횟수가 현재 상어의 사이즈와 같다면
        eatCount += 1
        if eatCount == sizeOfShark:
            sizeOfShark+=1
            eatCount = 0
