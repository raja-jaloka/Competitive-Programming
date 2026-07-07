#Problem 266 A {Stones On The Table}
n=int(input()) #total number of stones on table 
s=str(input()) #color-code seq of stones on the table

count=0
for i in range(n-1):
    if(s[i+1]==s[i]):
        count+=1
print(count)
