class Solution:
    def minTimeToType(self, word: str) -> int:
        t = 0
        cur = "a"
        for c in word:
            x = (ord(c)-ord(cur))%26
            t += min(x, 26-x)+1
            cur = c
        return t