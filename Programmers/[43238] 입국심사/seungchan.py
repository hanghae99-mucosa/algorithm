# 주어진 인풋이 크다 -> 이진탐색?
# 가장 빨리 끝나는 경우(모든 사람이 동시에 1분 걸리는 심사관들에게 진행)
# 가장 늦게 끝나는 경우(모든 사람이 가장 오래 걸리는 심사관에게 순차적으로 진행

def solution(n, times):
    low = 1
    high = n*max(times)

    # 계산한 시간(mid)내에 각 심사관이 몇명을 처리할 수 있는지 총합을 가지고 이분탐색 진행
    while (low<=high):
        mid = (low+high)//2
        count = 0
        for time in times:
            count += mid//time
        if count >= n:
            high = mid - 1
        else:
            low = mid + 1
    return low