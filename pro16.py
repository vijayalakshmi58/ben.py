than=int(input())
sung=list(map(int,input().split()))
jj=[1]*than
for i in range(than):
    if i==0:
        if sung[i]>sung[i+1]:
            jj[i]=jj[i]+jj[i+1]
    elif i>0:
        if sung[i]>sung[i-1]:
            jj[i]=jj[i]+jj[i-1]
print(sum(jj))
