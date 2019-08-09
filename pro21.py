viji1=int(input())
arg=list(map(int,input().split()))
sug1=int(viji1/2)
ram=arg[:sug1]
mag=arg[sug1::]
if ((sum(ram)//len(ram))==(sum(mag)//len(mag))):
    print("yes")
else:
    print("no")
