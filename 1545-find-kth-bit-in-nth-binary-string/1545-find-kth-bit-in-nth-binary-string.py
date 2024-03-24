class Solution:
    def findKthBit(self, n: int, k: int) -> str: 
        s = [0]
        l = 1
        while l<n:
            t = s+[1]+[1-x for x in reversed(s)]
            s = t
            l += 1
        return str(s[k-1])