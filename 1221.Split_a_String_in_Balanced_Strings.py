class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l1 = []
        r1 = []
        count =0
        for i in s:
            if i == 'L':
                l1.append(i)
            if i == 'R':
                r1.append(i)
            if len(l1) == len(r1) and len(l1) != 0 and len(r1) !=0:
                l1.clear()
                r1.clear()
                count += 1
        return count