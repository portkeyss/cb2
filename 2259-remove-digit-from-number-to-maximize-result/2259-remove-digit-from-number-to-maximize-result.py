class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = ""
        for i in range(len(number)):
            if number[i]==digit:
                x = number[:i]+number[i+1:]
                res = max(res, x)
        return res