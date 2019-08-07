nir,kind=map(int,input().split())
msg=list(map(int,input().split()))
msg.sort()
msg.reverse()
j=kind
pin=0
for i in msg:
    if(j>=i):
        any=int(j/i)
        pin=pin+any
        j=j-any*i
    if j==0:
        break
if(j==0):
   print(pin)
else:
   print("it's not posiible to select coins in such a way that they sum upto",kind)
