#SPOJ {Easy Math} 
nums=int(input())
for i in range(nums):
    l=str(input())
    l=l.split(' ')
    n,m,a,d=map(int,l)
    div1=a+d 
    div2=a+(2*d)
    div3=a+(3*d)
    div4=a+(4*d)
    count=0
    for i in range(n,m+1):
        if(i%a!=0):
            if(i%div1!=0):
                if(i%div2!=0):
                    if(i%div3!=0):
                        if(i%div4!=0):
                            count+=1 
    print(count)