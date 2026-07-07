#Codeforces Problem 405-A 
n=int(input())#total number of columns
na=str(input()) #number of blocks/column(str)

na=na.split(' ') #(str matrix)

#logic: the cubes fall to the right, therefore they must fall in an ascending order
for i in range(n):
    na[i]=int(na[i])

sorted_na=sorted(na)

for i in range(n):
    print(sorted_na[i], end=' ')
