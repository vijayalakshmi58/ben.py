beng=int(input())
viji=[]
jam=[]
for i in range(beng):
    viji.append(list(map(int,input().split())))
for sur in viji:
    for num in sur:
        jam.append(num)
jam.sort()
for i in jam:
    print(i,end=' ')
