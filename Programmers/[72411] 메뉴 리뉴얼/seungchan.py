# https://grazinggoat.notion.site/9-29-44cd8db520ff4508ae2818b2536ea923

# 조합 문제
# 각 손님의 주문 리스트에서 주어진 course들의 수의 조합을 추출
# 이렇게 만든 조합들을 카운트해서 2번 이상인것만 오름차순으로 정렬(by PQ)
from itertools import combinations
from queue import PriorityQueue

def solution(orders, course):
    answer = []
    dict = {}
    PQ = PriorityQueue()
    
    # 인덱스를 course에 주어진 수 그대로 씀
    candidateScore = [[0,""] for _ in range(course[-1]+1)]

    # 각 order들에 대해서 course들의 조합을 만들어 dict에 해당 조합의 경우의 수를 카운트
    for order in orders:
        # str to array
        order = list(order)

        # course에 주어진 케이스만 조합을 뽑으면 됨
        for i in course:
            for case in combinations(order, i):
                case = list(case)
                case.sort()
                case = ''.join(case)
                if case in dict:
                    dict[case] += 1
                else:
                    dict[case] = 1
    
    # dict의 카운트 값을 가지고 문자 길이별로 최대의 값을 찾기
    for key, value in dict.items():
        size = len(key)
        if value >= 2:
            if candidateScore[size][0]<value:
                candidateScore[size][0] = value
                candidateScore[size][1] = key
            elif candidateScore[size][0]==value:
                candidateScore[size][1] += (" "+key)
    
    # PQ에 넣어 오름차순 정렬
    for i in range(2,course[-1]+1):
        for menu in candidateScore[i][1].split():
            PQ.put(menu)

    while not PQ.empty():
        answer.append(PQ.get())
    
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))