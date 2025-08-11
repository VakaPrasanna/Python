Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
  
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
-----------------------------------------------------------------------
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    res. add(tuple([nums[i],nums[l],nums[r]]))
                    r-=1
                    l+=1
                elif sum<0:
                    l+=1
                else:
                    r-=1
        return list(res)   
        
                        
nums=list(map(int, input("Enter numbers: ").split()))
print(three_sum(nums))
----------------------------------------------------------------------
Enter numbers: -1 0 1 2 -1 -4
[[-1, -1, 2], [-1, 0, 1]]
