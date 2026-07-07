# CodeForces Problem 767-A {SnackTower}
n=int(input())
st=str(input())
st=list(map(int,st.split(" ")))
silo=[] #store here
sd=st.copy()
sd.sort()
sd=list(reversed(sd)) #Data Collection Done 
max_count=0

#Snack tower operation 
for i in range(n):
    if(st[i]==sd[max_count]):
        print(st[i],end=' ')
        max_count+=1
        for j in range(len(silo)):
            if(silo[j]==sd[max_count]):
                print(silo[j],end=' ')
                max_count+=1

        silo=[]
        print()
    else:
        silo.append(st[i])
        silo=sorted(silo, reverse=True)
        print()
        