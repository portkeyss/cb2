class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum(mat[i][i] for i in range(n))+sum(mat[i][n-1-i] for i in range(n))-(mat[n//2][n//2] if n%2==1 else 0)