def fun(nums,target):
    lst=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                for l in range(k+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        lst.append([nums[i],nums[j],nums[k],nums[l]])
    return lst if lst else 0

    
nums = [2, 2,2, 2, 2]
target = 8
print(fun(nums,target))
----------------------------------
121:
# cook your dish here
input=[7,1,5,3,6,4]
min_val=float('inf')
sum=0
for i in (input):
    if i<min_val:
        min_val=i
    elif i-min_val > sum:
        sum=i-min_val

print(sum)
------------------------------------------
