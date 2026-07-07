# UVA 10110 {Light, More Light} 
import math
n=int(input())
while(n!=0):
    sqrt=math.sqrt(n)
    sqrt=int(sqrt)
    if(sqrt*sqrt==n):
        print("yes")
    else: 
        print("no")
    n=int(input())

