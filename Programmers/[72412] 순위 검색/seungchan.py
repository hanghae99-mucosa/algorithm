from itertools import product
from bisect import bisect_left

# 주어지는 info를 가지고 각각 16가지의 조합을 만들수 있음
# 이를 점수와 함께 key, value 형식으로 저장
# value를 정렬
# 각각의 query를 key로 하여 value를 찾고
# value에서 이진 탐색을 통해 O(logN)만에 기준이 되는 scor의 위치를 찾음(그냥 정렬된 배열을 이동하며 찾는다면 O(n))

# 처음에 set을 이용하여 교집합이나 합집합 연산을 하고자 하였으나 이 또한 (매번 O(n))
def solution(info, query):
    answer = []
    allCase = {}
    cases = list(product([0,1],repeat=4))

    for i in range(len(info)):
        line = info[i].split()
        score = int(line[-1])

        for j in range(16):
            newKey=""
            for i in range(4):
                if cases[j][i] == 1:
                    newKey+=line[i]
                else:
                    newKey+="-"
            
            if newKey not in allCase:
                allCase[newKey] = []
            allCase[newKey].append(score)
                
    for value in allCase.values():
        value.sort()

    for i in range(len(query)):
        # query를 배열에 키워드 별로 담기
        line = query[i].split(" and ")
        line[-1], score = line[-1].split()
        score = int(score)
        
        line = ''.join(s for s in line)
        
        if line in allCase:
            target_list = allCase[line]
            idx = bisect_left(target_list, score)
            answer.append(len(target_list) - idx)
        else:
            answer.append(0)
        
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))