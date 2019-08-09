viji=int(input())
z=0
xen1=0
bg=[]
while z<90 and z<viji:
  s=0
  for j in str(viji-z):
    s+=int(j)
  if s+(viji-z)==viji:
    xen1+=1
    bg.append(viji-z)
  z+=1
print(xen1)
for z in bg:
  print(z)
