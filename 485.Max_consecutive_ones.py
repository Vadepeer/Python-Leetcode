class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i]: #to check the value is 1 or not 
                nums[i] = nums[i] + nums[i-1] #add the ith value and i-1th value inthe ith index
        return max(nums) #return the max value of the list
            