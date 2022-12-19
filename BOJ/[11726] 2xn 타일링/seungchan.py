# 방법의 수를 묻고 있고(DP는 optimum value를 찾거나 경우의 수를 찾을때)
# 직사각형을 왼쪽에서 차례로 채워나가는 형태이므로
# 이전의 더 작은 사이즈의 직사각형을 채우는 경우의 수와 관련이 있을듯 함
# -> 미래의 결정이 앞선 결정에 영향을 받음
# -> DP

# n크기의 직사각형의 경우의 수 = maze[n]이라고 했을때 (n>2)
# maze[i] = maze[i-1] + maze[i-2] 다음의 관계식을 가진다.

n = int(input())

def dp(n):
    # base case
    memo=[1,2]

    if n <= 2:
        return memo[n-1]

    # maze[i] = maze[i-1] + maze[i-2]
    for i in range(2,n):
        memo.append(memo[i-1]+memo[i-2])

    return memo[-1]%10007

print(dp(n))