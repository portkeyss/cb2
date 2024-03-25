class Solution:
    def numberOfWays(self, s: str) -> int:
        v = 1
        a = b = c = d = e = f = 0
        for ch in s:
            if ch=="1":
                c += b
                a += v
                e += d
            else:
                f += e
                d += v
                b += a
        return c+f        