class Solution:
    def reverseWords(self, s: str) -> str:
        string = ''
        lst = s.split()
        for i in lst:
            string += i[::-1]+' '
        return string.strip()
        