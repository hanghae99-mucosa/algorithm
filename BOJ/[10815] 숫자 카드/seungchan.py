n = int(input())
card = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

s = set(card)

for item in search:
    if item in s:
        print(1,end=' ')
    else:
        print(0,end=' ')