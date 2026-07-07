#Codeforces Problem 443-A{Anton and Letters}
l=[]
s=str(input())
s=s[1:-1]
if(len(s)==0):
    print(0)
else:
    l=s.split(", ")
    print(len(set(l)))