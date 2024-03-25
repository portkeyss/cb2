class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        A = dict()
        B = defaultdict(list)
        C = defaultdict(list)
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    A[k] = (i,j)
                    B[i].append(k)
                    C[j].append(k)
                    k += 1
        
        if k==0: return 0
        
        q = set([0])
        steps = 0
        while q:
            t = set()
            for mask in q:
                for bit in range(k):
                    if (1<<bit)&mask==0:
                        newMask = mask
                        r, c = A[bit]
                        for x in B[r]+C[c]:
                            newMask|=(1<<x)
                            if newMask==(1<<k)-1: return steps+1
                            t.add(newMask)
            q = t
            steps += 1         