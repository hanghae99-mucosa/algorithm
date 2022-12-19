# places 하나씩 검사하면 됨
# 각 사람의 위치에서 맨해튼 거리 2 이하인 곳을 모두 확인
# 그중에서 상하좌우(한칸), 상하좌우(두칸), 대각선의 경우를 나누어서 검사
# 각 경우마다 거리두기가 유지되는지 확인

def solution(places):
    answer = []

    def checkPlace(place):
        # 상하좌우(한칸)
        near = [[1,0],[0,1],[-1,0],[0,-1]]
        # 상하좌우(두칸)
        second = [[2,0],[0,2],[-2,0],[0,-2]]
        # 대각선
        diagonal = [[1,1],[-1,1],[-1,-1],[1,-1]]

        for i in range(5):
            place[i] = list(place[i])

        for x in range(5):
            for y in range(5):
                if place[x][y] == "P":
                    for dr in near:
                        nx = x + dr[0]
                        ny = y + dr[1]
                        # 바로 옆에 사람이 있는 경우
                        if 0<=nx<5 and 0<=ny<5 and place[nx][ny] == "P":
                            return 0
                        
                    for dr in second:
                        nx = x + dr[0]
                        ny = y + dr[1]
                        if 0<=nx<5 and 0<=ny<5:
                            # 두칸 옆에 사람이 있고 한칸 옆에 빈칸인 경우
                            if place[nx][ny] == "P" and place[int((nx+x)/2)][int((ny+y)/2)] == "O":
                                return 0
                    
                    for dr in diagonal:
                        nx = x + dr[0]
                        ny = y + dr[1]
                        if 0<=nx<5 and 0<=ny<5:
                            if place[nx][ny] == "P":
                                # 대각선에 사람이 있고 그 사이 양쪽에 모두 파티션이 있지 않은 경우
                                if not (place[nx][y] == "X" and place[x][ny] == "X"):
                                    return 0

        return 1

    for place in places:
        answer.append(checkPlace(place))
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))