# X의 최댓값이 1,000,000,000
# 시간복잡도가 N을 넘어가서는 시간 초과
# -> 이분 탐색

# 우승횟수가 늘어날때마다 게임횟수도 늘어남
# -> X와 Y 모두에 더해줘야함

# 부동소수점으로 인해 계산의 오류 발생
# -> 곱하기 연산을 먼저하고 나누기 연산을 이후

# X만큼 더하면 무조건 승률이 증가
# 그러나 Z가 99 이상이면 변동이 없음

X,Y = map(int,input().split())
Z = Y*100//X

start = 1
end = X

if Z >= 99:
    print(-1)

else:
    while (start<=end):
        mid = (start+end)//2
        candidateZ = (Y+mid)*100//(X+mid)
        if candidateZ<=Z:
            start = mid+1
        else:
            end = mid-1
    print(start)