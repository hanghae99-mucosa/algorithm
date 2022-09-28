# https://grazinggoat.notion.site/9-27-6751af5a584542a69c155ca846bb74c4

# 중복 순열
from itertools import product

def solution(n, info):
    answer=[]
    maxDiff=-1
    # 각 점수마다 이기거나 지는 경우의 수인 중복조합 케이스
    for case in product([0,1],repeat=11):
        lionScore = 0
        apeachScore = 0

        chance = n
        candidate = []

        isValid = True

        # 점수 계산
        for i in range(10,-1,-1):
            if case[i] == 1:
                lionScore += (10-i)

                # 이기는 경우이지만 남은 화살이 없음
                if chance - (info[i]+1) < 0:
                    isValid = False
                    break

                chance -= info[i]+1
                candidate.insert(0, info[i]+1)
            else:
                candidate.insert(0, 0)
                if info[i] != 0:
                    apeachScore += (10-i)
        
        if isValid == False:
            continue

        # 점수계산에서 이기지 않는 경우에는 무조건 0을 넣어주었음 
        # 남은 화살이 있는 경우 그것을 지는 케이스에 최대한으로 작은 점수부터 넣음
        if chance != 0:
            for i in range(10,-1,-1):
                if case[i] == 0 and info[i]>0:
                    if chance - info[i] >= 0:
                        candidate[i] = info[i]
                    else:
                        candidate[i] = chance
                        chance = 0
                        break
                

        # 어피치가 더 클 경우 다른 경우 or 화실이 남은 경우
        if lionScore <= apeachScore or chance!=0:
            continue
        
        else:
            diff = abs(apeachScore-lionScore)

            # 이전에 찾은 케이스보다 더 큰 점수차로 이긴 경우
            if maxDiff < diff:
                answer = candidate
                maxDiff = diff

            # 점수차이가 같은 경우
            elif maxDiff == diff:
                isLower = False
                
                for i in range(10,-1,-1):
                    if candidate[i] != 0 or answer[i] != 0:
                        if candidate[i]>answer[i]:
                            isLower=True
                        elif candidate[i]==answer[i]:
                            continue
                        else:
                            break
        
                if isLower:
                    answer = candidate
                    maxDiff = diff
        
    if maxDiff == -1:
        return [-1]
    else:
        return answer


    
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))