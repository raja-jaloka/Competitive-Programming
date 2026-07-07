# Codeforces Problem 282A
n=int(input())#the number of statements
x=0
for _ in range(n):
    s=str(input())
    if('++' in s):
        x+=1
    elif('--' in s):
        x-=1
print(x)
