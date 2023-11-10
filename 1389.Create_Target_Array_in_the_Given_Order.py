class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lst = []
        for i in range(len(index)):
            lst.insert(index[i],nums[i])
        return lst