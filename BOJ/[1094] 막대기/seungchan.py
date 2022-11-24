X = int(input())
count = 0

while X:
    if X%2 == 1:
        count += 1
    X//=2

print(count)