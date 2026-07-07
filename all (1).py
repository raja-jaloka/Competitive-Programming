#Problem 231A-codeforces A Team's dillema
n=int(input()) #Total number of problems
count=0 #Output the solvable problems

for _ in range(n):
    county=0 #number of 1's 
    prob=str(input()) #because integers are seperated by a single space char
    prob=prob.strip().split()
    #print(prob)
    for i in range(3):
        if(int(prob[i])==1):
            county+=1
    if(county>=2):
        count+=1
print(count)
