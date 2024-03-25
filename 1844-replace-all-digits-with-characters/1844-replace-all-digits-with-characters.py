class Solution:
    def replaceDigits(self, s: str) -> str:
        buffer = list(s)
        for i in range(1,len(s),2):
            buffer[i] = chr(ord(s[i-1])+int(s[i]))
        return "".join(buffer)