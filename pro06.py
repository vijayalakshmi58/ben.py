viji1=int(input())
viji2=list(map(int,input().split()))
ant=0
for x in range(len(viji2)-2):
    for y in range(x+1,len(viji2)-1):
        for z in range(y+1,len(viji2)):
            if viji2[x]<viji2[y]<viji2[z] and x<y<z:
                ant=ant+1
print(ant)
