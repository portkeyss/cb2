class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        A = [inf]*n
        for j in range(n):
            l = 0
            while j-l>=0 and j+l<n and s[j-l]==s[j+l]:
                if 2*l+1>=k:
                    A[j+l] = min(A[j+l],2*l+1)
                l+=1
            l = 0
            while j-l>=0 and j+l+1<n and s[j-l]==s[j+l+1]:
                if 2*l+2>=k:
                    A[j+l+1] = min(A[j+l+1],2*l+2)
                l+=1

        dp = [0]*(n+1)
        for i in range(k-1,n):
            dp[i+1] = dp[i]
            if A[i]<inf:
                dp[i+1] = max(dp[i+1],dp[i+1-A[i]]+1)
        return dp[n]