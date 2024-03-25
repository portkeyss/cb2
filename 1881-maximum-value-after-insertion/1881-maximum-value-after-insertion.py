class Solution:
    def maxValue(self, n: str, x: int) -> str:
        l = len(n)
        if n[0]=="-":
            i = 1
            while i < l and int(n[i])<=x:
                i += 1
            return n[:i]+str(x)+n[i:]
        i = 0
        while i < l and int(n[i])>=x:
            i += 1
        return n[:i]+str(x)+n[i:]