class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            s = set()
            for j in range(n):
                if matrix[i][j] in s: return False
                s.add(matrix[i][j])
        for j in range(n):
            s = set()
            for i in range(n):
                if matrix[i][j] in s: return False
                s.add(matrix[i][j])
        return True
                