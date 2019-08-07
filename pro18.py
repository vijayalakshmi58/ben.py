viji,sun=map(int,input().split())
sang=[]
tell=0
for i in range(viji):
    sang.append(list(map(int,input().split())))   
for i in range(viji):
    for j in range(sun-1):
        for k in range(j+1,sun+1):
            if sang[i][j:k]==[1]*len(sang[i][j:k]):
                 if all(sang[p+i][j:k]==[1]*len(sang[p+i][j:k]) for p in range(len(sang[i][j:k])-1)):
                     if len(sang[i][j:k])>tel:
                        tell=len(sang[i][j:k])
if len(sang)==1 and len(sang[0])==1 and sang[0][0]==1:
    print(1)
for i in range(tel):
    print(*[1]*tell)
