class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            count = 0
            if i == 0 or i == 1:
                lst.append(i)
                continue
            while i!= 0:
                count += i & 1
                i = i >> 1
            lst.append(count)
        return lst

            