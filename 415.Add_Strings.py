class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) < len(num2):
            num1 += '0' *(len(num2)-len(num1))
        else:
            num2 += '0'* (len(num1)-len(num2))
        result = ''
        car = 0
        for i in range(len(num1)):
            digit =int(num1[i])+int(num2[i])+car
            car = digit // 10
            result += str(digit % 10)
        if car > 0:
            result += str(car)
        return result[::-1]
