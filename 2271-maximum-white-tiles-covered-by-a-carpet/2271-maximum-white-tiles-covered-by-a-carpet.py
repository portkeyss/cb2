class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        A = []
        prev = -inf
        for a,b in tiles:
            if a==prev+1:
                A[-1][1] = b
            else:
                A.append([a,b])
            prev = b
            
        prefix = [[0,0,-1]]
        x = 0
        res = 0
        for a,b in A:
            prefix.append([a-1,x,1])
            x += b-a+1
            prefix.append([b,x,-1])
            if carpetLen>=b:
                res = max(res, x)
            else:
                j = bisect.bisect(prefix, [b-carpetLen+1])-1
                if prefix[j][2]==1:
                    res = max(res,x-prefix[j][1]-(b-carpetLen-prefix[j][0]))
                else:
                    res = max(res,x-prefix[j][1])
        return res