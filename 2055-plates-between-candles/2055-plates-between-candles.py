class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        n = len(s)
        res = []
        for i in range(n):
            if s[i]=="|":candles.append(i)
        for a,b in queries:
            i = bisect.bisect_right(candles, a-1)
            j = bisect.bisect_right(candles, b)-1
            x = 0
            if j>i:
                x = (candles[j]-candles[i]+1)-(j-i+1)
            res.append(x)
        return res        