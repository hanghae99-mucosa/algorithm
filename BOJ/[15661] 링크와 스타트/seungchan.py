# 팀을 나누는데 기본적으로 두팀으로 나누어짐
# 팀당 적어도 한명이 있어야하고 양팀 인원이 같을 필요는 없다
# -> 이진수로 표현 가능(모두 0과 모두 1인 경우 제외)

# 이진수로 팀을 나누고 그때마다 점수 계산해서 최소의 차이를 구하자

N = int(input())
info = [list(map(int,input().split()))for _ in range(N)]

minDiff = 19*100

for i in range(1,(1<<N)-1):
    count = 0   # 현재 배정될 사람 번호

    # 이진수에서 1인 팀
    score1=0
    team1=[]
    # 이진수에서 0인 팀
    score2=0
    team2=[]

    while i:
        if i%2 == 1:
            for num in team1:
                score1 += (info[num][count]+info[count][num])
            team1.append(count)
        else:
            for num in team2:
                score2 += (info[num][count]+info[count][num])
            team2.append(count)
        i//=2
        count+=1
    
    # 이진수로 표현했을때 N개의 자릿수로 표현되지 않는 경우
    # 모두 0이라고 가정하고 계산(ex: 0001)
    while count < N:
        for num in team2:
                score2 += (info[num][count]+info[count][num])
        team2.append(count)
        count += 1
    
    if minDiff > abs(score1-score2):
        minDiff = abs(score1-score2)

print(minDiff)