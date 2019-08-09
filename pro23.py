vg=int(input())
mag=2**vg
z=[]
for i in range(0,mag):
    l=bin(i)[2:].zfill(vg)
    if(len(l)<len(bin(2**vg-1)[2:])):
        z.append([l.count("1"),l])
    else:
        z.append([l.count("1"),l])
z.sort()
for i in range(len(z)):
    print(z[i][1])
