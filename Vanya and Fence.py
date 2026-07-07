# Codefoces 677-D2-A [Vanya and Fence]
l1=str(input()) #contains number and height
l1=l1.split(' ')
n=int(l1[0])
h=int(l1[1])
l2=str(input())
l2=l2.split(' ')
safe_width=0
for i in range(n):
    width=1
    ai=int(l2[i])
 
    if(ai>h):
        width=2
        
    safe_width+=width
    
print(safe_width)