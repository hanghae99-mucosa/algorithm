# s의 길이는 최대 1000
# O(n^2)이지만 n이 최대 500이므로 완전탐색 시간이 크지 않음
# -> 완전 탐색

# 최대 len(s)/2로 문자열 단위를 가져갈 수 있음
# len(s)/2부터 1까지 단위를 끊어보면서
# 직전 단위와의 비교를 통해 압축시킨 단어를 만듬
# 다 만든 단어의 길이를 이전에 만들었던 단어 길이와 비교 후 더 작다면 업데이트

def solution(s):
    half = int(len(s)/2)

    # 길이가 1인 s라면 half가 0이 됨 -> 1로 바꿔줌
    if half == 0:
        half = 1
    
    minLen = 1001
    
    # len(s)/2부터 1까지 단위를 끊어보면서
    for unit in range(half,0,-1):
        front = unit
        beforeS = s[:unit]
        count = 1
        newS = ""

        # 직전 단위와의 비교를 통해 압축시킨 단어를 만듬
        while True:
            if front+unit >= len(s):
                if beforeS == s[front:]:
                    count+=1
                    # count가 1일때는 숫자가 나타나지 않음
                    newS += (str(count) if count != 1 else "") + beforeS
                else:
                    newS += (str(count) if count != 1 else "") + beforeS + s[front:]
                    
                break

            else:
                if beforeS == s[front:front+unit]:
                    count+=1

                else:
                    newS += (str(count) if count != 1 else "") + beforeS
                    count = 1
                    beforeS = s[front:front+unit]

                front += unit
        
        # 다 만든 단어의 길이를 이전에 만들었던 단어 길이와 비교 후 더 작다면 업데이트
        if minLen > len(newS):
            minLen = len(newS)

    return minLen

print(solution("aaaaaa"))