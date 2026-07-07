# Codeforces Problem 770-A {New Password}
import random 
inp=str(input())
inp=inp.split(" ")
n=int(inp[0])
k=int(inp[1])
s='abcdefghijklmnopqrstuvwxyz'
w=['0' for _ in range(n)]
wb=['0' for _ in range(k)]
i=0 
j=random.randrange(0,26)
while(i!=k):
    if(s[j] not in wb):
        wb[i]=s[j]
        i+=1
        j=random.randrange(0,26) #we built the word_builder
        
print(wb)
        
x=random.randrange(0,k)
count=0 #number of pre-existing symbols 
i=0 #reinitialise the variable i to 0 to reuse it 
while(i!=n):
    if(i==0):
        w[i]=wb[x]
        i+=1 
        x=random.randrange(0,k)
    else:
        if(wb[x] in w ):
            if(count<n-k):
                if(w[i-1]!=wb[x]):
                    w[i]=wb[x]
                    i+=1
                    x=random.randrange(0,k)
                    count+=1 
                else:
                    x=random.randrange(0,k)
            else:
                x=random.randrange(0,k)
            
        else:
            w[i]=wb[x]
            i+=1 
            x=random.randrange(0,k)

s=''
for i in range(n):
    s+=w[i]

print(s)