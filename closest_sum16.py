16. 3Sum Closest

Description
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
------------------------------------------------------------
def fun(nums,target):
    closest_sum=float('inf')
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sum=nums[i]+nums[j]+nums[k]
                if abs(target-sum)< abs(target-closest_sum):
                    closest_sum=sum
    return closest_sum
nums = [-1,2,1,-4]
target = 1
print(fun(nums,target))
