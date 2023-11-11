class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            val = nums[i+1]
            while freq > 0:
                lst.append(val)
                freq -= 1
        return lst