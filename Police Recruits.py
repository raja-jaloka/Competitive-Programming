#Problem 427 A {Police Recruits}
n=int(input()) #total number of events 
s=str(input()) #Event-happenings

s=s.split(' ')

summ=0
count=0
for i in range(n):
    if(int(s[i])<0 and summ==0):
        count+=1
    elif(int(s[i])<0 and summ!=0):
        summ-=1
    elif(int(s[i])>0):
        summ+=int(s[i])
print(count)
