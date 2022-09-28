# https://grazinggoat.notion.site/9-28-8f6f02ef76054bcc9cce6aff66cb0e60


def solution(survey, choices):
    answer = ''
    scoreSum =[[0,0],[0,0],[0,0],[0,0]]
    score = [3,2,1,0,1,2,3]
    dict = {"RT":[0,0], "TR":[1,0], "FC":[0,1], "CF":[1,1], "MJ":[0,2], "JM":[1,2], "AN":[0,3], "NA":[1,3]}

    for i in range(len(survey)):
        agreeType = dict[survey[i]][0]
        indicator = dict[survey[i]][1]

        if agreeType == 0:
            if choices[i]>=4:
                scoreSum[indicator][1]+=score[choices[i]-1]
            else:
                scoreSum[indicator][0]+=score[choices[i]-1]
        else:
            if choices[i]>=4:
                scoreSum[indicator][0]+=score[choices[i]-1]
            else:
                scoreSum[indicator][1]+=score[choices[i]-1]

    for i in range(4):
        if i==0:
            if scoreSum[i][0] >= scoreSum[i][1]:
                answer += "R"
            else:
                answer += "T"
        elif i==1:
            if scoreSum[i][0] > scoreSum[i][1]:
                answer += "F"
            else:
                answer += "C"
        elif i==2:
            if scoreSum[i][0] > scoreSum[i][1]:
                answer += "M"
            else:
                answer += "J"
        else:
            if scoreSum[i][0] >= scoreSum[i][1]:
                answer += "A"
            else:
                answer += "N"
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))