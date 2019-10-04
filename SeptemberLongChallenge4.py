import math
t = int(input())
for i in range(t):
    delta = input()
    delta = delta.split()
    for j in range(2):
        delta[j]=int(delta[j])
    if(delta[0]==1):
        if delta[1]==1:
            print(1)
        else:
            print(-1)
        continue
    if(delta[0]==2):
        if(delta[1]==2):
            print(2)
            continue
    temp1 = (delta[0]*(delta[0]-1))//2 + delta[0]
    if delta[1]>temp1:
        print(-1)
        continue
    if(delta[1]==temp1):
        print(delta[0])
        continue


    if delta[1]<delta[0]-1:
        print(-1)
        continue
    if delta[1]==delta[0]-1 or delta[1]<=delta[0]+1:
        if delta[0]==2:
            print(1)
        else:
            print(2)
        continue
    ans = 3
    if delta[1]<=2*delta[0]:
        print(ans)
        continue
    temp2 = delta[0]//2
    delta[1]=delta[1]-2*delta[0]
    ans += (delta[1]//temp2)+ (delta[1]%temp2>0)
    print(ans)
