vg=int(input())
leg=input().split()
sg=[]
for i in range(vg):
    san=leg[i]
    for j in range(i+1,vg):
        if(int(leg[i])<int(leg[j]))and (int(leg[j-1])<int(leg[j])):
            san+=leg[j]
        else:
            break
    sg.append(len(san))
print(max(sg))
