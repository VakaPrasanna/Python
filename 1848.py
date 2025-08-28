nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0
min_diff=float('inf')
for i in range(start,len(nums)):
    if nums[i]==target:
        if abs(i-start)<min_diff:
            min_diff=abs(i-start)
print(min_diff)

#return min(abs(i - start) for i, x in enumerate(nums) if x == target)
