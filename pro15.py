viji=input()
sung=map(int,input().split())
jam=[]
for i in sung:
    eat=bin(i)
    jam.append(eat)
fine=sorted(jam)
fine.reverse()
for j in fine:
    print(int(j,2))
