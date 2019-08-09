vg = int(input())
lg = list(map(int, input().split()))
maximum = 0
tsp = 0
any = lg[0]
for i in range(0,vg-1):
    if any < lg[i+1]:
        tsp +=1
        any = lg[i+1]
    else:
        if max(lg[i+1:]) < any:
            any = lg[i+1]
print(tsp+1)
