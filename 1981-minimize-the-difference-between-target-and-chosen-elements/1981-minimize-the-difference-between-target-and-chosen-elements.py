class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        a = set([0])
        for i in range(m):
            b = set()
            for j in range(n):
                z = inf
                for x in a:
                    y = mat[i][j]+x
                    if y<=target:
                        b.add(y)
                    elif y<z:
                        b.add(y)
                        z = y
            a = b
        res = inf
        for x in a:
            res = min(res,abs(x-target))
        return res