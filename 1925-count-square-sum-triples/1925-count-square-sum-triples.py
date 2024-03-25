class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for c in range(n+1):
            for b in range(1,c):
                x = c*c-b*b
                y = int(sqrt(x))
                if x==y*y:
                    res += 1
        return res
                        