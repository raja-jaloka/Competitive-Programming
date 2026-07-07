# UVA 10110 {Light, More Light} 
n=int(input())
while(n!=0):
    count=0 
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count%2==0):
        print("no")
    else:
        print("yes")
        
    n=int(input())

