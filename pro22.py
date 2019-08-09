sgn=int(input())
vg=list(map(int,input().split()))[:sgn]
t=sum(vg[0:sgn:2])
jum=sum(vg[1:sgn:2])
if t>jum:
  print(t)
else:
  print(jum)
