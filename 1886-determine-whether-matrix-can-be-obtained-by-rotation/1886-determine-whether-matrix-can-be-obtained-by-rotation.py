class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        return all(mat[i][j]==target[i][j] for i in range(n) for j in range(n)) or all(mat[j][n-1-i]==target[i][j] for i in range(n) for j in range(n)) or all(mat[n-1-i][n-1-j]==target[i][j] for i in range(n) for j in range(n)) or all(mat[n-1-j][i]==target[i][j] for i in range(n) for j in range(n))