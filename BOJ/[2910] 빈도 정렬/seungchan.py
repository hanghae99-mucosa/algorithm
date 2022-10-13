# 입력된 수열을 하나씩 확인하면서
# 최초 입력되었다면 최초 입력된 등수를 기록
# 그리고 해당 숫자를 카운트
# 이후에 카운트와 최초 입력된 등수를 가지고 정렬 후 프린트

# C가 입력 최댓값을 주의하여 count를 dict가 아닌 list로 만들시 메모리 초과 발생

N, C = map(int,input().split())
nums = list(map(int, input().split()))

# 나왔던 순서와 빈도를 저장하는 변수
# 숫자 : [최초 등장, 빈도]
counts = {}

index = 0
for i in range(len(nums)):
    num  = nums[i]

    # 해당 숫자가 처음 나왔다면
    if num not in counts:
        counts[num] = [N-i,1]
    else:
        counts[num][1] += 1

counts = sorted(counts.items(), key = lambda x: (x[1][1],x[1][0]), reverse=True)

for count in counts:
    num = count[0]
    count = count[1][1]

    for i in range(count):
        print(num,end=' ')