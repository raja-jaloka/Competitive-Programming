#CodeForces Problem-768-A {Oath Of The Night's Watch}
n=int(input())#number of stewards
l=str(input())#string of strength stewards
l=list(map(int,l.split(" "))) #integer list of strength of stewards
#print(l)
def mbin_search(i,k):
    count_less=0
    count_greater=0
    if(i>0):
        l_left=l[:i]
        for j in range(len(l_left)):
            if(l_left[j]<k):
                count_less=1
            elif(l_left[j]>k):
                count_greater=1
                    
    if(i+1<len(l)):
        l_right=l[i+1:]
        for j in range(len(l_right)):
            if(l_right[j]<k):
                count_less=1
            elif(l_right[j]>k):
                count_greater=1
                
    return count_greater+count_less
    
agg_count=0
for i in range(len(l)):
    count=mbin_search(i,l[i])
    if(count==2):
        agg_count+=1

print(agg_count)