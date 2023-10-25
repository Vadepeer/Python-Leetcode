class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first=second=third = float('-inf') #Make the first,second and third value are -infinity
        uniq_nums = set(nums)#make it unique values
        for i in uniq_nums:
            if i > first:#compare the values assign them into following
                third = second
                second = first
                first = i
            elif i > second:
                third  = second
                second = i
                
            elif i > third:
                third = i
                
        return third if len(uniq_nums) >= 3 else first