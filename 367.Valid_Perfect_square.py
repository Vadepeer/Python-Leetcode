class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # for i in range(1, num //2+2):
        #     if i*i==num:return True
        #     if i*i>num:return False
        if int(num**0.5)*int(num**0.5) == num: #Get the root value of the num and multiply
            return True
        else: 
            return False
        