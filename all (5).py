# Codeforces problem 158A [Next Round]

#Input Initialisation 
l=str(input()) #contains both n and k space separated 
l=l.split(' ')
n=int(l[0])
k=int(l[1])

m=str(input())
m=m.split(' ')
for i in range(n):
    m[i]=int(m[i])
#print(m,type(m[i]))
val=m[k-1]
count=0
for i in range(n):
    if(m[i]!=0):
        if(m[i]>=val):
            count+=1
print(count)