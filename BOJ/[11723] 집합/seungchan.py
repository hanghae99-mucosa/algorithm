import sys

M = int(input())
S = [0 for i in range(21)]

for _ in range(M):
    action = sys.stdin.readline().strip().split()

    if action[0]=="add":
        S[int(action[1])]=1
    elif action[0]=="remove":
        S[int(action[1])]=0
    elif action[0]=="check":
        if S[int(action[1])]==1:
            print(1)
        else:
            print(0)
    elif action[0]=="toggle":
        S[int(action[1])]=(S[int(action[1])]+1)%2
    elif action[0]=="all":
        for i in range(1,21):
            S[i]=1
    else:
        for i in range(1,21):
            S[i]=0