#CodeForces 474-A {Keyboard}
Shift=str(input())
alpha=str(input())
l1=['q','w','e','r','t','y','u','i',"o","p"]
l11=set(l1)
l2=['a','s','d','f','g','h','j','k','l',';']
l22=set(l2)
l3=['z','x','c','v','b','n','m',',','.','/']
l33=set(l3)
if(Shift=="L"):
    Shift=+1
else:
    Shift=-1 

alpha1=[0 for i in range(len(alpha))]

for i in range(len(alpha)):
    if(alpha[i] in l11):
        inx=l1.index(alpha[i])
        alpha1[i]=l1[inx+Shift]
    if(alpha[i] in l22): 
        inx=l2.index(alpha[i])
        alpha1[i]=l2[inx+Shift]
    if(alpha[i] in l33):
        inx=l3.index(alpha[i])
        alpha1[i]=l3[inx+Shift]
        
a=''
for i in range(len(alpha1)):
    a+=alpha1[i]
print(a)