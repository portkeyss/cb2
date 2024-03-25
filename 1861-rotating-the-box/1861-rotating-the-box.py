class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        res = [["."]*m for _ in range(n)]
        for i in range(m):
            k = n-1
            for j in range(n-1,-1,-1):
                if box[i][j] == "*":
                    k = j
                    res[k][m-1-i] = "*"
                    k -= 1
                elif box[i][j] == ".": continue
                else:
                    res[k][m-1-i] = "#"
                    k -= 1
        return res