#Codeforces Problem 381-A 
n=int(input())#total number of cards on the table
t=str(input()) #numbers on the card on the table(str)

t=t.split(" ") #matrix of str

#t=reversed(sorted(t)) #can't reverse using reversed because then the list will not be subscriptable

sereja=0 
dima=0 
lit=t.copy() #lit=t causes mutations which we want to avoid
maxi=0
for i in range(n):
    lit[i]=int(lit[i])

while(lit!=[]):
    #sereja's turn
    if(lit[-1]>lit[0]):
        sereja+=lit[-1]
        lit.remove(lit[-1]) #This is safe to do because every number is distinct
    else:
        sereja+=lit[0]
        lit.remove(lit[0])
    
    #Dima's turn
    if(lit!=[]):
        if(lit[-1]>lit[0]):
            dima+=lit[-1]
            lit.remove(lit[-1]) #This is safe to do because every number is distinct
        else:
            dima+=lit[0]
            lit.remove(lit[0])
    


print(sereja,end=' ')
print(dima)