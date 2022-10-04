# https://grazinggoat.notion.site/9-29-44cd8db520ff4508ae2818b2536ea923

# 기준점에서 가까운 순서로 익은 토마토가 전파가 됨 -> BFS
# 익은 사과가 1초가 지났을때 동시에 다른 곳으로 전파됨
# 큐에 삽입시 익은 사과의 모든 위치를 한번에 넣고 꺼내야함

from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

def bfsForBox(M, N, box):
    visited = [[0 for _ in range(M)]for _ in range(N)]
    numOfApple = 0
    ripeApple = []
    day = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # 초기 익은 토마토 위치 셋팅 & 안 익은 사과 갯수 카운트
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                visited[i][j] = 1
                ripeApple.append([i,j])
            elif box[i][j] == 0:
                numOfApple += 1

    # 익은 사과 모두 동시에 인접 사과로 전파되는 것
    # 큐에서 꺼낸다는거는 1초가 지났을때 행위를 처리하겠다는 것
    # 큐에 삽입할때 현재 익은 사과의 모든 위치를 동시에 넣고 동시에 꺼내줘야함
    Q = deque([ripeApple])

    while Q:
        ripeApple = Q.popleft()

        if numOfApple == 0:
            break
        
        newRipeApple = []

        for apple in ripeApple:
            
            for i in range(4):
                nx, ny = apple[0] + dx[i], apple[1] + dy[i]
                
                if 0 <= nx < N and 0 <= ny < M:
                    if box[nx][ny] == 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[apple[0]][apple[1]]+1
                        numOfApple -= 1
                        newRipeApple.append([nx,ny])    #새로 익은 사과들의 위치만 담음
        
        day+=1
        
        # 새로 익은 사과가 있는 경우에만 큐에 넣음
        # 그렇지 않으면 빈 배열이 큐에 들어가 무한 루프 위험 
        if len(newRipeApple) != 0:
            Q.append(newRipeApple)  # 익은 사과들의 모든 위치를 담고 있는 배열을 큐에 넣음 
                    
    if numOfApple != 0:
        return -1
    else:
        return day

print(bfsForBox(M,N,box))