class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1,dic2 = {},{}#In this approach we use hash map
        for i in set(t): #Get the count value of  each element in t
            dic1[i] = t.count(i)
        for j in  set(s):#Get the count value of each element in s
            dic2[j] = s.count(j)
        for k in dic1: #Compare dic1 and dic2 find the difference & return the value
            if k not in dic2:
                return k
            if dic1[k] != dic2[k]:
                return k