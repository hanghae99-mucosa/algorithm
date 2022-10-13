# 전형적인 MST 문제
# Kruskal과 Prim 알고리즘 두가지 방식 존재

# Kruskal
# weight가 작은 edge부터 사이클을 형성하지 않으면 MST의 edge로 채택
# 사이클 생성 여부는 Union-Find로 확인

# Prim
# 최초에 임의의 vertice 하나를 선택하여 T에 포함
# 이후 T에 포함되어있지 않은 vertice와 T 사이의 최소 거리를 업데이트
# 그중에서도 최소 거리를 가지는 vertice를 T에 포함
# 이를 모든 T가 포함 될때까지 시행

############### solution - Kruskal ###############
def makeRoot(size, input):
    for i in range(size):
        input.append(i)
    return input


def find(x, root):
    while x != root[x]:
        x = root[x]
    return x


def union(x, y, root, rank):
    rootX = find(x, root)
    rootY = find(y, root)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            root[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            root[rootX] = rootY
        else:
            root[rootY] = rootX
            rank[rootX] = rank[rootX] + 1

def connected(x, y, root):
    return find(x, root) == find(y, root)

############### solution - Kruskal ###############

N = int(input())
M = int(input())
costs = [list(map(int, input().split()))for _ in range(M)]

# 비용을 기준으로 오름차순 정렬
costs = sorted(costs, key=lambda x: x[2])

# 각 요소의 루트를 초기화
root = []
rank = [0 for _ in range(N)]
makeRoot(N, root)

# MST 비용
total = 0

for cost in costs:
    # 서로 연결되어 있지 않다면
    if not connected(cost[0]-1,cost[1]-1,root):
        union(cost[0]-1,cost[1]-1,root, rank)
        total += cost[2]

############### solution - Prim ###############
N = int(input())
M = int(input())

# 지금까지 만든 MST와 나머지 edge 사이의 최소 거리
currentCost = {i : float('inf') for i in range(N)}
currentCost[0] = 0

# 각 컴퓨터 사이 비용을 key, value 형식으로 저장
costs = {}
for _ in range(M):
    a, b, cost = map(int, input().split())
    costs[(a-1,b-1)] = cost
    costs[(b-1,a-1)] = cost

total = 0
while currentCost:
    # 현재 MST와 연결하기 위한 코스트가 가장 작은 컴퓨터
    com = min(currentCost,key=currentCost.get)
    # MST에 포함 시켰으므로 제거
    total += currentCost.pop(com)
    # 이후 새로 만들어진 MST를 기준으로 currentCost 업데이트
    for nextCom in currentCost:
        if (com, nextCom) in costs:
            currentCost[nextCom] = min(currentCost[nextCom],costs[(com,nextCom)])

print(total)