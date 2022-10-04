#

def solution(enroll, referral, seller, amount):
    answer = []
    dict = {}
    result = {}

    # 자신을 참여시킨 조직원 정보를 담은 dict
    for i in range(len(enroll)):
        dict[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        earn = amount[i]*100
        user = seller[i]

        share = updateResult(result, earn, user)
        
        # 더 이상 자신을 참여시킨 조직원이 없을때 or share가 0일 경우 모두 루프 종료
        while True:
            if dict[user]!="-":
                user = dict[user]
                share = updateResult(result, share, user)
                if share == 0:
                    break
            else:
                break
    
    for user in enroll:
        if user in result:
            answer.append(result[user])
        else:
            answer.append(0)

    return answer

def updateResult(result, earn, user):
    share = int(earn/10)
    profit = earn-share
        
    if user in result:
        result[user] += profit
    else:
        result[user] = profit
    
    return share