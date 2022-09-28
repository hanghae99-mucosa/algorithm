# https://grazinggoat.notion.site/9-27-6751af5a584542a69c155ca846bb74c4

# 출발 지점과 도착 지점이 주어짐
# 가장 빠른 시간을 구함
# 한번 움직이는데 드는 비용이 1초로 동일
# 이동한 거리로 보는것이 아니라 이동한 횟수의 관점에서 보면 한번 움직인 거리도 동일
# -> BFS

from collections import deque

n, k = map(int, input().split())

def find(n, k):
    visited = [0 for _ in range(100001)]

    # 시작위치 셋팅
    visited[n] = 1

    # 걷기 or 순간이동 
    move = [-1, 1, 2]

    # list.pop(0)의 time complexity O(N) -> deque사용-O(1)
    Q = deque()
    Q.append(n)

    while Q:
        n = Q.popleft()

        if n == k:  # 목적지 도착
            return visited[n]-1
        
        for i in range(3):
            if i == 2:
                nextN = n * move[i]
            else:
                nextN = n + move[i]
            
            if 0 <= nextN <= 100000: # 영역 확인
                if visited[nextN] == 0:  # 방문하지 않은곳
                    visited[nextN] = visited[n] + 1
                    Q.append(nextN)
    
print(find(n,k))