#Codeforces Problem 731-A {Night At The Musuem}
name=str(input()) #enter the name 
name=name.lower()
string='abcdefghijklmnopqrstuvwxyz'
curr=0
turn=0

def mod(k):
    if(k>0):
        return k 
    else:
        return -k
    

for i in range(len(name)):
    loc_str=name[i]
    loc=string.index(name[i])
    #print(loc,end=' ')
    k=curr-loc
    k=mod(k)
    #print(k,end=' ')
    if(k!=0):
        st=mod(26-k)
        dt=k 
        if(st<=dt and st!=0):
            turn+=st 
        else:
            turn+=dt 
        curr=loc
        #print(turn)
print(turn)