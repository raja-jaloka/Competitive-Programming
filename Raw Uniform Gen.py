# UVA 408{Uniform Generator} 
x=str(input())
x=x.split(' ')
step=int(x[0])
mod=int(x[1])
nat=[i for i in range(mod)]
step_nat=[-1 for i in range(mod)]
step_x=0
i=0
while(step_x not in step_nat):
    if(i==0):
        step_nat[i]=step_x
        step_x=(step_x+step)%mod 
        i+=1 
    else:
        step_nat[i]=step_x
        step_x=(step_x+step)%mod 
        i+=1

step_nat.sort()
if(nat==step_nat):
    print("Good Choice ")
else:
    print("Bad Choice")


    
