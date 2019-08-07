viji,than=map(int,input().split())
list3=list(map(int,input().split()))
viji=[]
list3.insert(0,0)
for y in range(than):
     vin=[]
     s=0
     vg,ii=map(int,input().split())
     for i in range(vg,ii+1):         
         s^=list3[i]     
     viji.append(s)
for y in viji:
     print(y)
