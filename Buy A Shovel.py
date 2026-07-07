# Codeforces Problem 732-A {Buy A Shovel}
n=str(input()) #contains k and r  
n=n.split(" ")
k=int(n[0])
r=int(n[1])
n=0 #number of shovels
for i in range(1,10):
    if((k*i)%10==0):
        n=i 
        break
    elif((k*i)%10==r):
        n=i 
        break 
print(n)