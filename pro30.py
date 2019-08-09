vg1=(input())
cat1=0
for i in range(0,len(vg1)):
    sur1=(vg1[:i]+vg1[i+1:])
    if(int(sur1) % 8==0):
        cat1=1
        break
if(cat1==1):
    print("yes")
else:
    print("no")
    
    
