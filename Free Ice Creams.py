#Codeforces Problem 686-A{Free Ice Cream}
l=str(input())#contains n and x 
l=l.split(" ")
n=int(l[0])
x=int(l[1])
distress=0
for i in range(n):
    x_=str(input())
    x_=x_.split(" ")
    sign=x_[0]
    d=int(x_[1])
    if(sign=='+'):
        x+=d
    else:
        if(x>=d):
            x-=d
        else:
            distress+=1
print(f'{x} {distress}')