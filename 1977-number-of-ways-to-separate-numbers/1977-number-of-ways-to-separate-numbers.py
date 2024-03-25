class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0]=="0": return 0
        mod = 10**9+7
        n = len(num)
        #find the longest common substring
        same = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,i,-1):
                same[i][j] = (same[i+1][j+1]+1)*(num[i]==num[j])

        dp = [[0]*(n+1) for _ in range(n+1)]
        for j in range(n):
            for l in range(1,j+1,1):
                if num[j+1-l]=="0":
                    dp[j+1][l] = dp[j+1][l-1]
                elif j+1-2*l<0:
                    dp[j+1][l] = (dp[j+1][l-1]+dp[j+1-l][j+1-l])%mod
                else:
                    commonLength = same[j+1-2*l][j+1-l]
                    if commonLength>=l or num[j+1-2*l+commonLength]<num[j+1-l+commonLength]:
                        dp[j+1][l] = (dp[j+1][l-1]+dp[j+1-l][l])%mod
                    else:
                        dp[j+1][l] = (dp[j+1][l-1]+dp[j+1-l][l-1])%mod
            dp[j+1][j+1] = (dp[j+1][j]+1)%mod
        return dp[n][n]