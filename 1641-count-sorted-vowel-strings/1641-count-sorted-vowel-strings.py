class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1]*5 #dp is the count of words starting with a,e,i,o,u
        for _ in range(2,n+1):
            dp[3]+=dp[4]
            dp[2]+=dp[3]
            dp[1]+=dp[2]
            dp[0]+=dp[1]
        return sum(dp)