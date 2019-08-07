viji,thang = input().split()
thang = int(thang)
faked = False
beng = list(map(int,input().split()))
for i in range(len(beng)):
    for j in range(len(beng)):
        if beng[i]+beng[j] == thang:
            faked = True
print("yes" if faked else "no") 
