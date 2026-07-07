# Codeforces Problem 709-A {Juicer}
l1=str(input()) # contains n,b,d 
l1=l1.split(" ")
n=int(l1[0])
b=int(l1[1])
d=int(l1[2])
l2=str(input())
l2=l2.split(" ")

summ=0 
dump=0 

for i in range(n):
     
        
    if(int(l2[i])<=b):
       summ+=int(l2[i])
       if(summ>d):
           dump+=1 
           summ=0

        
print(dump)