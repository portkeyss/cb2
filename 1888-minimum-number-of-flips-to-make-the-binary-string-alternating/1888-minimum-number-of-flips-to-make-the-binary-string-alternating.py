class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        prefix = [0] #cumulative mismatch against 010101...
        for i,c in enumerate(s):
            mismatch = (c==("0" if i%2==0 else "1"))
            prefix.append(prefix[-1]+mismatch)
        if n%2==0:
            return min(prefix[n], n-prefix[n])
        
        res = inf
        for i,c in enumerate(s):
            a = prefix[i+1]+n-i-1-(prefix[n]-prefix[i+1])
            res = min(res, a, n-a)
        return res