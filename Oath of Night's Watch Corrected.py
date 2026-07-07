#CodeForces Problem-768-A {Oath Of The Night's Watch}
n=int(input())#number of stewards
l=str(input())#string of strength stewards
l=list(map(int,l.split(" "))) #integer list of strength of stewards
m=max(l)
s=min(l)
agg=0
for i in range(n):
    x=l[i]
    if(x>s and x<m):
        agg+=1
print(agg)