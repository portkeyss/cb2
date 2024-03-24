class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        A = targetGrid
        bounds = defaultdict(lambda:[inf,-inf,inf,-inf])

        m,n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                x = A[i][j]
                bounds[x][0] = min(bounds[x][0],i)
                bounds[x][1] = max(bounds[x][1],i)
                bounds[x][2] = min(bounds[x][2],j)
                bounds[x][3] = max(bounds[x][3],j)

        def peelable(y):
            i,j,k,l = bounds[y][0],bounds[y][1], bounds[y][2], bounds[y][3]
            for p in range(i,j+1):
                for q in range(k,l+1):
                    if A[p][q]!=y and A[p][q]>0: return False
            return True

        def peel(y):
            i,j,k,l = bounds[y][0],bounds[y][1], bounds[y][2], bounds[y][3]
            for p in range(i,j+1):
                for q in range(k,l+1):
                    A[p][q] = 0
        
        s = []
        for x in bounds.keys():
            if peelable(x): s.append(x)
        
        while s:
            while s:
                x = s.pop()
                peel(x)
                bounds.pop(x)
            for x in bounds.keys():
                if peelable(x): s.append(x)
        return not bounds    