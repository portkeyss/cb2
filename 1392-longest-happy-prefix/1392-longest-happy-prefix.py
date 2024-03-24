class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0]*n #longest prefix suffix
        i = 1
        j = 0
        while i<n:
            if s[i]==s[j]:
                j += 1
                lps[i] = j
                i += 1
            elif j>0:
                j = lps[j-1]
            else:
                i += 1
        return s[:j]