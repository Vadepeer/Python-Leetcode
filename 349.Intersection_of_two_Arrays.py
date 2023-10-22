class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in nums1:
            if i in nums2 and i not in lst:#check the num1 value in the num2 list
                lst.append(i)
        return lst