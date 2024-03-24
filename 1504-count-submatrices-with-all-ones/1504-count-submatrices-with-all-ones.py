class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        H = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            A = [None]*n
            B = [None]*n
            for j in range(n):
                if mat[i][j]==0:
                    H[i][j]=0
                elif i==0: 
                    H[i][j]=1
                else: 
                    H[i][j] = 1+H[i-1][j]
            stack = []
            for j in range(n):
                while stack and H[i][stack[-1]]>=H[i][j]:
                    stack.pop()
                A[j] = stack[-1] if stack else -1
                stack.append(j)
            stack = []
            for j in range(n-1,-1,-1):
                while stack and H[i][stack[-1]]>H[i][j]:
                    stack.pop()
                B[j] = stack[-1] if stack else n
                stack.append(j)
            for j in range(n):
                res += H[i][j]*(j-A[j])*(B[j]-j)
        return res       