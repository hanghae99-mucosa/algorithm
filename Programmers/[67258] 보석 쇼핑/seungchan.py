# 효율성 테스트가 있는 문제는 O(n)에 해결될 수 있는 알고리즘이 있는가 생각해보자
# 배열 인덱스를 담고 있는 start와 end index를 선언하고
# end index를 증가시키며 모든 보석 종류를 담을 수 있는 가장 작은 end index 탐색(1)
# 이후 start index를 증가시키며 여전히 모든 보석 종류를 담을 수 있는 가장 큰 start index 탐색(2)
# 찾은 가장 큰 start index를 1 증가시키고 다시 1번 단계로 돌아간다(3)
# 이를 end index가 gems의 끝에 도달할때까지 시행한다.(4)
# -> 투포인터 알고리즘

from collections import defaultdict

def solution(gems):
    answer = []
    start, end = 0,0
    
    s = set()
    # start와 end 사이 나오 gem들의 빈도수
    count = defaultdict(int)
    # end와 i 사이 나오 gem들의 빈도수
    tmpCount = defaultdict(int)

    # 첫 start와 end를 구할때 gems의 모든 gem을 확인하여 set을 만듬
    for i in range(len(gems)):
        tmpCount[gems[i]] += 1
        # 이전에 나온적이 없는 gem이 나온 경우
        if gems[i] not in s:
            end = i
            s.add(gems[i])
            # count를 tmpCount를 가지고 업데이트
            for key, val in tmpCount.items():
                count[key] += val
            # tmpCount 초기화
            tmpCount = defaultdict(int)
    
    # start를 늘여가며 모든 종류의 gem을 가지는 확인
    while True:
        count[gems[start]] -= 1
        # 해당 gem이 0이라는 것은 한 종류의 gem이 없는 경우
        if count[gems[start]] == 0:
            break
        start += 1
    
    
    answer= [start+1,end+1]
    length = end-start
    # 없어진 gem이므로 찾아야함
    findGem = gems[start]
    # 없어진 gem 다음 위치로 start 이동
    start += 1

    # 이를 end index가 gems의 끝에 도달할때까지 시행한다.(4)
    while end != len(gems)-1:
        end+=1
        count[gems[end]]+=1
        # 없어진 gem을 찾음
        if gems[end] == findGem:
            # start를 늘여가며 모든 종류의 gem을 가지는 확인
            while True:
                count[gems[start]] -= 1
                if count[gems[start]] == 0:
                    break
                start += 1
            # 새로 찾은 영역이 이전의 영역보다 짧을때
            if length > (end - start):
                length = end-start
                answer= [start+1,end+1]
            findGem = gems[start]
            start += 1
            
    return answer
