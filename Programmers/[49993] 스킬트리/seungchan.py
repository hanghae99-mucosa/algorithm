# skill_trees의 있는 요소 하나씩
# skill에 있는 원소만 순서대로 뽑아서 새로운 문자를 만들고
# 그 문자를 skill의 순서와 일치하는지 비교

def solution(skill, skill_trees):
    answer = 0
    skillSet = set(skill)

    def checkOrder(check):
        i = 0
        for l in check:
            if l == skill[i]:
                i+=1
            else:
                return False

        return True

    # skill_trees의 있는 요소 하나씩
    for skill_tree in skill_trees:
        check = ""

        # skill에 있는 원소만 순서대로 뽑아서 새로운 문자를 만들고
        for s in skill_tree:
            if s in skillSet:
                check+=s

        # 그 문자를 skill의 순서와 일치하는지 비교
        if checkOrder(check):
            answer+=1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))