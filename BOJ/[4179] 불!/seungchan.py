# 주의할 점
# F는 여러개가 주어질 수 있고 없을 수도 있음(예외 처리 필요)
# 불이 이동하고 난후 지훈이가 이동한다고 생각해아함(지훈이가 먼적 그 자리로 이동했더라고 하더라도 불이 그곳에 이동한다면 지훈이는...)

# 지훈이는 가장 가까운 경로로 탈출하고자 하고 불은 자신의 위치에서 가까운곳부터 확산이 된다.
# -> bfs 적용

# 지훈이와 불 모두 이동하는 주체라고 생각하고 두 주체를 위한 각각의 visited 배열을 생성
# 큐에 최초 위치를 삽입하고
# 지훈이 큐와 불의 큐에서 현재 이동 시간(count)인 것은 전부 꺼내어 bfs 시행(이 부분 핵심)
# 만약 꺼낸것이 미로 영역 밖이므로 visited를 출력
# 큐가 다 소진되어 종료 되었음에도 return을 하지 않았다면 탈출 경로가 없는 것

from collections import deque

R,C = map(int,input().split())
maze = []
jLocation=[]
fLocations=[]
time = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 지훈이와 불의 방문비용 이차원 리스트
jVisited = [[0 for _ in range(C)]for _ in range(R)]
fVisited = [[0 for _ in range(C)]for _ in range(R)]

# 인풋을 받으며 지훈이 위치와 불의 위치를 확인
for i in range(R):
    row = list(input()) 
    for j in range(C):
        if row[j] == "J":
            jLocation = [i,j]
            row[j] = "."
        elif row[j] == "F":
            fLocations.append([i,j])
            row[j] = "."
    maze.append(row)

def bfs(R,C):
    # 현재 이동 시간
    count = 0

    # 지훈이의 시작 위치 셋팅 및 큐 삽입
    jVisited[jLocation[0]][jLocation[1]] = 1
    jQ = deque([(jLocation[0], jLocation[1])])
    
    # 불의 시작 위치 셋팅 및 큐 삽입
    if len(fLocations)!=0:
        fQ = deque([])
        for fLocation in fLocations:
            fVisited[fLocation[0]][fLocation[1]] = 1
            fQ.append((fLocation[0], fLocation[1]))

    while jQ:
            count+=1
            if len(fLocations)!=0:
                # 현재 이동 시간과 일치하는 위치는 다 꺼내어서 다음 이동 확인(불)
                while fQ:
                    fx, fy = fQ.popleft()
                    # 현재 이동 시간과 일치하지 않는 경우 반복문 종료
                    if count != fVisited[fx][fy]:
                        fQ.appendleft((fx, fy))
                        break
                    for i in range(4):
                        if len(fLocations)!=0:
                            nfx, nfy = fx + dx[i], fy + dy[i]
                            if 0 <= nfx < R and 0 <= nfy < C:
                                if maze[nfx][nfy] == "." and fVisited[nfx][nfy] == 0:
                                    fVisited[nfx][nfy] = fVisited[fx][fy] + 1
                                    fQ.append((nfx, nfy))
            
            # 현재 이동 시간과 일치하는 위치는 다 꺼내어서 다음 이동 확인(지훈이)
            while jQ:
                jx, jy = jQ.popleft()
                # 현재 이동 시간과 일치하지 않는 경우 반복문 종료
                if count != jVisited[jx][jy]:
                    jQ.appendleft((jx, jy))
                    break
                for i in range(4):
                    njx, njy = jx + dx[i], jy + dy[i]
                    if 0 <= njx < R and 0 <= njy < C:
                        # 불이 아직 방문하지 않은 경우
                        if maze[njx][njy] == "." and jVisited[njx][njy] == 0 and fVisited[njx][njy]==0:
                            jVisited[njx][njy] = jVisited[jx][jy] + 1
                            jQ.append((njx, njy))
                    else:
                        return jVisited[jx][jy]
                
    return "IMPOSSIBLE"

print(bfs(R,C))