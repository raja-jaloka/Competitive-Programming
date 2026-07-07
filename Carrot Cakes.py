#Codeforces Problem 799-A {Carrot Cakes}
l=str(input())
l=l.split(" ")
n=int(l[0])
t=int(l[1])
k=int(l[2])
d=int(l[3])
if(n>k):
    original_time=((n+k-1)//k)*t
    cakes_baked=0
    res_time=0
    tab=0
    built_flag=0
    while(cakes_baked<n):
        if(built_flag==0):
            built_flag=1
            tab=max(d,t)
            if(tab==d):
                cakes_baked=(((d-t)//t)*k)+k #the extra k is cakes baked for oven 1 
                res_time=(d-t)%t
            elif(tab==t):
                cakes_baked=k
                res_time=abs(d-t)
        else:
            tab+=t  
            cakes_baked+=2*k 
    tab-=res_time
    if(tab<original_time):
        print("YES")
 
    else:
        print("NO")
else:
    print("NO")
    
