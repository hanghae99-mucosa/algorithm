# 진실을 아는 사람과 같은 파티에 있었다면 그 곳에 모두는 진실을 아는 사람
# 그렇게 진실을 알게 된 사람이 다른 파티에 가게된다면 그곳에 있는 모두도 진실을 아는 사람
# 서로 연결되어 있으면 모두 진실을 아는 사람이 됨
# 서로 연결되어 있음을 표시하기에 적합한 -> union-find를 이용

n, m = map(int,input().split())
fact = list(map(int,input().split()))
root = [-1]
persons =[]

def makeRoot(size,root):
    for i in range(1,size+1):
        root.append(i)
    return root

def find(x,root):
    if x == root[x]:
        return x;
    root[x] = find(root[x],root)
    return root[x]

def union(x,y,root):
    rootX = find(x,root)
    rootY = find(y,root)

    if rootX != rootY:
        root[rootY] = rootX
    
    return root

def connected(x,y,root):
    return find(x,root) == find(y,root)

# root 초기화
makeRoot(n,root)

# 진실을 아는 사람들을 root를 모두 통일
for i in fact[1:]:
    root[i] = fact[1]

# m개의 파티원 정보를 받으면서
for i in range(m):
    row = list(map(int, input().split()))
    persons.append(row[1:])

    # 같은 파티에 참석한 사람은 union
    for i in range(1,row[0]):
        union(row[i],row[i+1],root)

# 진실을 아는 사람이 미존재
if fact[0] == 0:
    print(m)

# 진실을 아는 사람 존재
else:
    # 각 파티에 파티원들을 진실을 아는 팀원들과 connected 되어있는지 확인
    for person in persons:
        for p in person:
            if connected(p,fact[1],root):
                m-=1
                break
    print(m)

