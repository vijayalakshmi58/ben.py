viji=int(input())
ar=list(map(int,input().split()))
sug=int(viji/2)
ram=ar[:sug]
mag=ar[ans::]
if ((sum(ram)//len(ram))==(sum(mag)//len(mag))):
    print("yes")
else:
    print("no")
