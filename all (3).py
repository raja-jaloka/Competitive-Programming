# Codeforces Problem 2172E
n=int(input())#the number of tests conducted
num1=0
num2=0
for _ in range(n):
    s=str(input()) #first line code 
    s=s.split(' ')
    base_code=s[0]
    j=int(s[1])
    k=int(s[2])
    
    if(len(base_code)==2): #num initialisation of 2 digit numbers
        if(j==1):
            num1="12"
        else: 
            num1="21"
        if(k==1):
            num2="12"
        else: 
            num2="21"
    elif(len(base_code)==3): #num initialisation of 3 digit numbers
        if(j>=1 and j<=2):
            if(j==1):
                num1="123"
            elif(j==2):
                num1="132"
        elif(j>=3 and j<=4):
            if(j==3):
                num1="213"
            elif(j==4):
                num1="231"
        elif(j>=5 and j<=6):
            if(j==5):
                num1="312"
            elif(j==6):
                num1="321" 
                
        if(k>=1 and k<=2):
             if(k==1):
                 num2="123"
             elif(k==2):
                 num2="132"
        elif(k>=3 and k<=4):
            if(k==3):
                num2="213"
            elif(k==4):
                num2="231"
        elif(k>=5 and k<=6):
            if(k==5):
                num2="312"
            elif(k==6):
                num2="321"
    
    elif(len(base_code)==4):#num initialisation of 4 digit number
        if(j>=1 and j<=6):
            if(j==1):
                num1="1234"
            elif(j==2):
                num1="1243"
            elif(j==3):
                num1="1324"
            elif(j==4):
                num1="1342"
            elif(j==5):
                num1="1423"
            elif(j==6):
                num1="1432"
        elif(j>=7 and j<=12):
            if(j==7):
                num1="2134"
            elif(j==8):
                num1="2143"
            elif(j==9):
                num1="2314"
            elif(j==10):
                num1="2341"
            elif(j==11):
                num1="2413"
            elif(j==12):
                num1="2431"
        elif(j>=13 and j<=18):
            if(j==13):
                num1="3124"
            elif(j==14):
                num1="3142"
            elif(j==15):
                num1="3214"
            elif(j==16):
                num1="3241"
            elif(j==17):
                num1="3412"
            elif(j==18):
                num1="3421"
        elif(j>=19 and j<=24):
            if(j==19):
                num1="4123"
            elif(j==20):
                num1="4132"
            elif(j==21):
                num1="4213"
            elif(j==22):
                num1="4231"
            elif(j==23):
                num1="4312"
            elif(j==24):
                num1="4321" #j end 4
    
        if(k>=1 and k<=6):
            if(k==1):
                num2="1234"
            elif(k==2):
                num2="1243"
            elif(k==3):
                num2="1324"
            elif(k==4):
                num2="1342"
            elif(k==5):
                num2="1423"
            elif(k==6):
                num2="1432"
        elif(k>=7 and k<=12):
            if(k==7):
                num2="2134"
            elif(k==8):
                num2="2143"
            elif(k==9):
                num2="2314"
            elif(k==10):
                num2="2341"
            elif(k==11):
                num2="2413"
            elif(k==12):
                num2="2431"
        elif(k>=13 and k<=18):
            if(k==13):
                num2="3124"
            elif(k==14):
                num2="3142"
            elif(k==15):
                num2="3214"
            elif(k==16):
                num2="3241"
            elif(k==17):
                num2="3412"
            elif(k==18):
                num2="3421"
        elif(k>=19 and k<=24):
            if(k==19):
                num2="4123"
            elif(k==20):
                num2="4132"
            elif(k==21):
                num2="4213"
            elif(k==22):
                num2="4231"
            elif(k==23):
                num2="4312"
            elif(k==24):
                num2="4321"
    x=0 
    y=0 
    for i in range(len(num1)):
        for j in range(len(num2)):
            if(i==j and num1[i]==num2[j]):
                x+=1
            elif(i!=j and num1[i]==num2[j]):
                y+=1 
    print(f'{x}A{y}B')