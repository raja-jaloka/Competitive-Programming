# CodeForces Problem 136-A {Presents}
n=int(input())
s=str(input())
s=s.split(" ")
i,j=0,0
js=[0 for i in range(n)]
while(j<n):
    if(j+1==int(s[i])):
        js[j]=i+1 
        j+=1
        i=0
    else:
        i+=1 
for i in range(n):
    print(js[i],end=' ')
