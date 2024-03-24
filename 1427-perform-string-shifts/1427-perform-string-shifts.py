class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = 0
        for p in shift:
            if p[0] == 0:
                n -= p[1]
            else:
                n += p[1]
        n = n % len(s)
        print(n)
        return s[len(s)-n:] + s[:len(s)-n]