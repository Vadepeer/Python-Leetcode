class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst = []
        lst.append(nums[0])
        for i in range(0,len(nums)-1):
            lst.append(nums[i+1]+lst[i])
        return lst 