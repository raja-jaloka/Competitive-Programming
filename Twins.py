#Codeforces Problem 160-A {Twins}
n=int(input())
coins=str(input())
coins=list(map(int, coins.split(" ")))
total=sum(coins)
mysum=0
count=0 
coins=sorted(coins,reverse=True)

for i in range(len(coins)):
    mysum=sum(coins[:i+1])
    count+=1 
    if(mysum>(total-mysum)):
        break 
print(count)