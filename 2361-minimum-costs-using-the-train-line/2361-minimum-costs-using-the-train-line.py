class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        a, b = 0, expressCost
        res = [0]*n
        for i,(r,e) in enumerate(zip(regular,express)):
            a1 = min(a+r, b+e)
            b1 = min(b+e, a+r+expressCost)
            a, b = a1, b1
            res[i] = min(a,b)
        return res