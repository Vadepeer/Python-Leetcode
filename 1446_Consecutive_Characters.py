class Solution:
    def maxPower(self, s: str) -> int:
        count,maxi = 1,0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                if count > maxi:
                    maxi = count
                count =1
        return max(maxi,count)
