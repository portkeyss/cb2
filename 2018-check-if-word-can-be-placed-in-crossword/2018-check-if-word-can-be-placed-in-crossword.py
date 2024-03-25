class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m,n,k = len(board), len(board[0]), len(word)
        
        def check(w):
            for i in range(m):
                prevBlock = -1
                for j in range(n+1):
                    if j==n or board[i][j]=="#":
                        if j-prevBlock-1==k and all(board[i][prevBlock+1+p] in [" ", w[p]] for p in range(k)):
                            return True
                        prevBlock = j

            for j in range(n):
                prevBlock = -1
                for i in range(m+1):
                    if i==m or board[i][j]=="#":
                        if i-prevBlock-1==k and all(board[prevBlock+1+p][j] in [" ", w[p]] for p in range(k)):
                            return True
                        prevBlock = i
            return False
        
        return check(word) or check(word[::-1])