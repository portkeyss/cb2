class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9+7
        m, n = len(words), len(words[0])
        
        dp = [[0]*n for _ in range(len(target))] #dp[k][j] is the total number of possible ways to form target[:k+1] using {words}[:j+1]
        for j in range(n):
            A = Counter()
            for i in range(m):
                A[words[i][j]]+=1
            for k in range(len(target)):
                old = dp[k][j-1] if j>0 else 0
                new = 0
                if k==0: new = A[target[k]]
                elif j>0:
                    new = (A[target[k]]*dp[k-1][j-1])%mod
                dp[k][j] = (old+new)%mod
        return dp[len(target)-1][n-1]