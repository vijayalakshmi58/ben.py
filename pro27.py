viji,ss=map(int,input().split())
ts=list(map(int,input().split()))
tsp=list(map(int,input().split()))
thn=[]
cin=0
for i in range(viji):
    x=tsp[i]/ts[i]
    thn.append(x)
while jj>=0 and len(thn)>0:
    mindex=thn.index(max(thn))
    if jj>=ts[mindex]:
        cin=cin+tsp[mindex]
        jj=jj-ts[mindex]
    ts.pop(mindex)
    tsp.pop(mindex)
    thn.pop(mindex)
print(cin)
