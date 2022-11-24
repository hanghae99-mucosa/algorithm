# 점수의 최댓값을 물었다
# 이전에 밟은 계단에 따라 현재 밟을수 있는 계단이 달라짐
# (이전의 결정이 다음 결정에 영향을 줌)
# -> DP
# -> 점화식을 도춣하자

# base case가 필요하다 (f(1),f(2)는 명확)
# f(x) = max(f(x-2),f(x-3)+x-1위치의 점수) + x위치의 점수

N = int(input())
stairs = [int(input()) for i in range(N)]

def climb(N):
    memo = [0,stairs[0],sum(stairs[:2])]
    
    for i in range(2,N):
        memo.append(max(memo[(i-2)+1],memo[(i-3)+1]+stairs[i-1])+stairs[i])
    
    return memo[-1]

print(climb(N))