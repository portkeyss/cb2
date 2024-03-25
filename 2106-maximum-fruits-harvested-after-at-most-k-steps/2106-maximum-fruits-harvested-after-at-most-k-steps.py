class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        A = [[-inf,0]]
        for p,a in fruits:
            A.append([p, a+A[-1][1]])
        A.append([inf,A[-1][1]])
        
        res = 0
        s1 = bisect.bisect(A, [startPos,inf])-1
        s2 = bisect.bisect(A, [startPos-1,inf])
        l = bisect.bisect(A, [startPos-k-1,inf])
        r = bisect.bisect(A, [startPos+k,inf])-1
        
        for i in range(l,r+1):
            if A[i][0]<=startPos:
                d = startPos-A[i][0]
                x = 2*A[i][0]+k-startPos
                j = max(s1,bisect.bisect(A, [x, inf])-1)
                res = max(res, A[j][1]-A[i-1][1])
            else:
                d = A[i][0]-startPos
                x = 2*A[i][0]-k-startPos
                j = min(s2, bisect.bisect(A, [x-1, inf]))
                res = max(res, A[i][1]-A[j-1][1]) 
        return res