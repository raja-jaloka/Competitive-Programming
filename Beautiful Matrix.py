#Codeforces problem 263 A {Beautiful Matrix}

#initialise the matrix 
mat=[[0 for _ in range(5)] for _ in range(5)]

#Replace the 0's in the matrix with the correct values given in the input.
for i in range(5):
    l=str(input())
    l=l.split(" ")
    for j in range(5):
        mat[i][j]=int(l[j])

#Find the i,j with the value 1
x=-1 #x-coordinate of 1 value 
y=-1 #y-coordinate of 1 value 
for i in range(5):
    for j in range(5):
        if(mat[i][j]==1):
            x=i
            y=j 

#Perform Swaps
swaps=0
while(x!=2):
    if(x<2):
        x+=1
        swaps+=1
    else:
        x-=1
        swaps+=1
while(y!=2):
    if(y<2):
        y+=1
        swaps+=1 
    else:
        y-=1 
        swaps+=1 

print(swaps)