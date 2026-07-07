#Codeforces 567-A {LineLand Mail}
n=int(input())
nums=str(input())
nums=nums.split(" ")
maxi=float('-inf')
mini=float('inf')
for i in range(n):
    if(i==0 or i==n-1):
        if(i==0):
            maxi=abs(int(nums[i])-int(nums[n-1]))
            mini=abs(int(nums[i])-int(nums[i+1]))
        else:
            maxi=abs(int(nums[i])-int(nums[0]))
            mini=abs(int(nums[i])-int(nums[i-1]))
    else:
        if(abs(int(nums[i])-int(nums[n-1]))>abs(int(nums[i])-int(nums[0]))):
            maxi=abs(int(nums[i])-int(nums[n-1]))
        else:
            maxi=abs(int(nums[i])-int(nums[0]))
        if(abs(int(nums[i])-int(nums[i-1]))>abs(int(nums[i])-int(nums[i+1]))):
            mini=abs(int(nums[i])-int(nums[i+1]))
        else:
            mini=abs(int(nums[i])-int(nums[i-1]))
    print(f'{mini} {maxi}')
