class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        st =''
        if len(s) < len(words):
            return False
        else:
            for i in range(len(words)):
                if words[i][0] == s[i]:
                    st += s[i]
                else:
                    return False
        return st == s