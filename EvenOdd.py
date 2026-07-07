#codeforces problem 318-A {Even Odds} 
st=str(input())
st=st.split(" ")
n=int(st[0])
k=int(st[1])
if(n%2==0):
    mid=n//2
else:
    mid=(n+1)//2

l=[]
for i in range(1,n+1,2):
    l.append(i) #Odd Append
for i in range(2,n+1,2):
    l.append(i) #Even Append 

#searching for element at k-1th position 
print(l[k-1])
