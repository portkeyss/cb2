class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s)-1
        while l<r:
            if s[l]==s[r]:
                a = l
                while a<r and s[a]==s[l]: a += 1
                if a==r: return 0
                b = r
                while s[b]==s[r]: b -= 1
                l, r = a, b
            else:
                break
        return r-l+1