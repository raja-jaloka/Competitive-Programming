#Codeforces Problem 520-A {Pangram}
n=int(input())#length of the string 
s=str(input())#string 
flag=False
s=set(s.lower()) #set so that redundancy is reduced
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

if(n<26):
    flag=False
else:
    for let in alpha:
        if(let in s):
            flag=True
        else:
            flag=False 
            break
        
if(flag==False):
    print("NO")
else:
    print("YES")