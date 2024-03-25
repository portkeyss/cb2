class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        
        def isNice(x,y):
            st = set(s[x:y+1])
            for a in st:
                if a.islower() and a.upper() not in st or a.isupper() and a.lower() not in st: return False
            return True
        
        res = ""
        for i in range(n):
            for j in range(i,n):
                if isNice(i,j) and j-i+1>len(res):
                    res = s[i:j+1]
        return res