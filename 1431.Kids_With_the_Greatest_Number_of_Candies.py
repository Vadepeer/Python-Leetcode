class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        val = max(candies)
        lst = []
        for i in candies:
            if i+extraCandies >= val:
                lst.append(True)
            else:
                lst.append(False)
        return lst