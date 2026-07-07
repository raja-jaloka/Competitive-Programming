# Codeforces Problem 431-A {Black Square}

a=str(input())
a=a.split(' ') 
s=str(input())
sum_cal=0
for i in range(len(s)):
    index=int(s[i])
    sum_cal+=int(a[index-1])
    
print(sum_cal)
