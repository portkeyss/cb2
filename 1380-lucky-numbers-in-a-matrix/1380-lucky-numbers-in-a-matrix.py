class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        minInRow = [min(row) for row in matrix]
        maxInCol = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        luckies = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==minInRow[i]==maxInCol[j]: luckies.append(matrix[i][j])
        return luckies