viji1,jj1=map(int,input().split())
ts=list(map(int,input().split()))
tsp=list(map(int,input().split()))
thn=[]
cin=0
for i in range(viji1):
    x=tsp[i]/ts[i]
    thn.append(x)
while jj1>=0 and len(thn)>0:
    mindex=thn.index(max(thn))
    if jj1>=ts[mindex]:
        cin=cin+tsp[mindex]
        jj1=jj1-ts[mindex]
    ts.pop(mindex)
    tsp.pop(mindex)
    thn.pop(mindex)
print(cin)
