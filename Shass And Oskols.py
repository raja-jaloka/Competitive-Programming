# Codeforces Problem 294-A {Shass and Oskols}
n=int(input()) #number of lines 
lin_arr=str(input())
lin_arr=lin_arr.split(" ")
for i in range(n):
    lin_arr[i]=int(lin_arr[i])

m=int(input())

for _ in range(m):
    linx=str(input())
    linx=linx.split(" ")
    x=int(linx[0])-1
    y=int(linx[1])
    if(x-1==-1):
        lin_arr[x+1]+=lin_arr[x]-y
        lin_arr[x]=0
    if(x+1==n):
        lin_arr[x-1]+=y-1
        lin_arr[x]=0
    elif(x-1!=-1 and x+1!=n):
        lin_arr[x-1]+=y-1 
        lin_arr[x+1]+=lin_arr[x]-y 
        lin_arr[x]=0

for i in range(n):
    print(lin_arr[i])