class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for i in sentences:
            if len(i.split()) > maxi:
                maxi = len(i.split())
        return maxi
        