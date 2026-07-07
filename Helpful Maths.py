#Codeforces 339-A {Helpful Math}
l=str(input())
l=l.split("+")
l.sort() #Solved Using sort() i.e Timsort
r=''
for i in range(len(l)):
    r+=l[i]+'+'
    
print(r[:-1])
