viji,sun1=map(int,input().split())
sang1=[]
tel1=0
for i in range(viji):
    sang1.append(list(map(int,input().split())))   
for i in range(viji):
    for j in range(sun1-1):
        for k in range(j+1,sun1+1):
            if sang1[i][j:k]==[1]*len(sang1[i][j:k]):
                 if all(sang1[p+i][j:k]==[1]*len(sang1[p+i][j:k]) for p in range(len(sang1[i][j:k])-1)):
                     if len(sang1[i][j:k])>tel1:
                        tel1=len(sang1[i][j:k])
if len(sang1)==1 and len(sang1[0])==1 and sang1[0][0]==1:
    print(1)
for i in range(tel1):
    print(*[1]*tel1)
