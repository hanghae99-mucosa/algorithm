# 자신의 순서가 n이라고 했을때
# 다음 라운드의 나의 순서는 (n/2)를 반올림 한 순서가 된다

# round로 반올림시 0.5는 내림이 된다
# -> 주의하자

from math import ceil

def solution(n,a,b):
    answer = 1

    while b!= a:
        a = ceil(a/2)
        b = ceil(b/2)
        if b == a:
            return answer
        else:
            answer += 1

print(solution(16, 7, 8))