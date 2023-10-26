class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lst = []
        num1 = set(nums)
        for i in range(1,len(nums)+1):
            if i not in num1:
                lst.append(i)
        return lst