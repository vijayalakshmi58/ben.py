vg,tt=map(int,input().split())
bear=[]
for i in range(0,vg):
    ag=[int(sv) for sv in input().split()]
    bear.append(sorted(ag))
for i in range(0,len(bear[0])):
  #print(bear[i])
  for j in range(0,len(bear)-1):
    if bear[j][i]>bear[j+1][i]:
      bear[j][i],bear[j+1][i]=bear[j+1][i],bear[j][i]
for i in bear:
  print(*i)
