# 경우의 수는 최대 3!로 6개
# -> 완전 탐색

# 숫자와 연산자를 분리하여 큐에 담음
# 큐에서 pop을 하면서 현재 계산하고자하는 연산자가 나오면 계산을 해서 다시 새로운 큐에 넣고
# 아니라면 그냥 새로운 큐에 넣음

from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0

    def operate(beforeNum, afterNum, operator):
        if operator == "*":
            result = int(beforeNum) * int(afterNum)
        elif operator == "+":
            result = int(beforeNum) + int(afterNum)
        else:
            result = int(beforeNum) - int(afterNum)
        return str(result)


    ops = ["*","+","-"]
    maxDiff = -1

    # 숫자와 연산자를 분리하여 큐에 담음
    li = []
    s = 0
    for i, l in enumerate(expression):
        if l in ops:
            li.append(expression[s:i])
            li.append(l)
            s=i+1
    li.append(expression[s:])

    # 나타나지 않은 연산자는 순열에서 제외
    for op in ops:
        if op not in expression:
            ops.remove(op)

    #  순열을 만들고
    for operators in permutations(ops):
        ques = [deque(li),deque()]

        # 꺼내고자하는 큐와 넣고자하는 큐의 위치
        q1 = 0
        q2 = 1

        # 순열을 통해 만들어진 케이스에서 연산자를 하나씩 꺼내서
        for operator in operators:
            while len(ques[q1]):
                item = ques[q1].popleft()
                # 큐에서 pop을 하면서 현재 계산하고자하는 연산자가 나오면 계산
                if len(ques[q2]) and ques[q2][-1] == operator:
                    ques[q2].pop()
                    item = operate(ques[q2].pop(),item,operator)
                ques[q2].append(item)
            # 큐의 위치를 바꾸어줌
            q1, q2 = q2, q1
        
        # 계산한 값의 절댓값
        diff = abs(int(ques[q1].pop()))

        # 이전에 계산한 결과보다 크다면 업데이트
        if diff > maxDiff:
            maxDiff = diff
        
    return maxDiff

print(solution("100-200*300-500+20"))
