from itertools import combinations
import copy

N, K = map(int, input().split())

# 기본으로 주어지는 접두사, 접미사 학습을 위한 글자
char = [False for _ in range(26)]
char[ord('a')-ord('a')] = True
char[ord('n')-ord('a')] = True
char[ord('t')-ord('a')] = True
char[ord('i')-ord('a')] = True
char[ord('c')-ord('a')] = True

basic = copy.deepcopy(char)

# 새로 학습해야하는 글자
newChar = []

# 단어 하나라도 알려면 최소한의 학습 글자수 감소
K-=5

# 읽을수 있는 단어의 수
maxCount = 0

words = []
for _ in range(N):
    str = input()
    word=set()
    for c in str[4:-4]:
        # 새로 학습해야하는 문자라면
        if char[ord(c)-ord('a')] is False:
            char[ord(c)-ord('a')] = True
            newChar.append(c)
        # 현재 입력된 단어에서 a,n,t,i,c를 제외한 단어인 경우
        if basic[ord(c)-ord('a')] is False:
            word.add(c)
    words.append(word)


# 접두사, 점미사도 학습할 시간이 없는 경우
if K<0:
    print(maxCount)
# 모든 알파벳 학습 가능한 경우
elif K == 21:
    print(N)
else:
    # combination 하는데 K가 newChar의 갯수보다 크면 조합이 생성 안됨
    if len(newChar) < K:
        K = len(newChar)
    # 학습할 문자를 뽑아서
    for case in combinations(newChar,K):
        count = 0
        for word in words:
            matchCount = 0
            for c in case:
                # 뽑은 문자가 주어진 단어와 일치하는지
                if c in word:
                    matchCount += 1
            # 뽑은 문자들로 주어진 단어 학습 가능하다면
            if matchCount == len(word):
                count+=1
        if count>maxCount:
            maxCount = count
    print(maxCount)
    