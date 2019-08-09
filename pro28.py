viji=int(input())
vg=list(map(int,input().split()))
vg.sort()
sin1=0
spv=0
for i in range(len(vg)):
    if vg[i]>=sin1:
        spv=spv+1
    sin1=sin1+vg[i]
print(spv)
