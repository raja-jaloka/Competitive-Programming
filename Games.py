# Codeforces Problem 268-A {GAMES}
n=int(input()) #number of teams
home=[0 for _ in range(n)]
guest=[0 for _ in range(n)]
count=0
for i in range(n):
    s=str(input())
    s=s.split(" ")
    home[i]=s[0]
    guest[i]=s[1]

for i in range(n):
    for j in range(n):
        if(i!=j):
            if(home[i]==guest[j]):
                count+=1
                
print(count)
    