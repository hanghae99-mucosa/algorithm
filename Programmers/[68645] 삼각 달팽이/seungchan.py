# 위에서 부터 아래로 내려가면서 한개씩 넣고
# 제일 아래 줄에 도달할떄는 한변을 다 채워서 넣고
# 다시 올라오면서 한변을 채우고
# 위의 행위를 반복

def solution(n):
    # 각 줄의 숫자를 담아둔 변수
    answer = [[] for _ in range(n)]
    # 각 줄에 현재 들어가야할 숫자의 위치
    rowDir = [0 for _ in range(n)]
    # 현재 넣고자하는 줄
    row = 0
    # 진행 방향(아래로: True, 위로: False
    dirFlag = True
    # 현재 넣어야하는 수
    count = 1

    # 넣어야하는 수의 최댓값
    maxCount = 0
    for i in range(1,n+1):
        maxCount += i

    while count<=maxCount:
        # 삼각형 밑변에 넣는 경우
        if row == n-1 and dirFlag:
            for j in range(rowDir[row],row-rowDir[row]+1):
                answer[row].insert(j,count)
                count += 1
            row -= 1
            n -= 1
            dirFlag = False

        # 삼각형 한칸씩 내려가면서 넣는 경우
        elif dirFlag:
            answer[row].insert(rowDir[row],count)
            row += 1
            count += 1

        # 삼각형 한칸씩 올라가면서 넣는 경우
        else:
            answer[row].insert(rowDir[row]+1,count)
            rowDir[row] += 1
            row -= 1
            count += 1
        
        # 이미 해당 줄에 다 넣은 경우
        if len(answer[row])==row+1:
            if dirFlag:
                row-=2
                dirFlag = False
            else:
                row+=2
                dirFlag = True
    
    result = []
    for each in answer:
        result.extend(each)
    return result

print(solution(10))