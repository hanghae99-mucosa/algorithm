def solution(p):

    def makeStr(p):
        # 1. 빈 문자열이라면 그냥 리턴
        if p == "":
            return p
        else:
            # 2. u와 v로 분리
            leftCount = 0
            rightCount = 0

            for i in range(len(p)):
                if p[i] == "(":
                    leftCount += 1
                else:
                    rightCount += 1
                
                if leftCount == rightCount:
                    break
            
            u = p[:i+1]
            v = p[i+1:]

            # 3. u가 올바른 문자열
            if u[0] == "(" and u[-1] == ")":
                return u+makeStr(v)
            # 4. u가 올바른 문자열 아님
            else:
                newU = ""
                for i in u[1:-1]:
                    newU += (")" if i == "(" else "(")

                return "(" + makeStr(v) + ")" + newU


    return makeStr(p)

print(solution("()))((()"))