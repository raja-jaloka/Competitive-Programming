#codeforces problem 318-A {Even Odds} 
import time 
st=str(input())
st=st.split(" ")
n=int(st[0])
k=int(st[1])-1
a=time.time()
if(n%2==0):
    mid=n//2
else:
    mid=(n+1)//2

if(k<mid):
    print(2*(k)+1)
elif(k==mid):
    print(2)
else:
    print(2*(k-mid)+2)