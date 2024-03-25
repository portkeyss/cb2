class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = 0
        dp =[0]
        sm = 0
        for i in range(n):
            sm += nums[i]
            mx = max(mx, nums[i])
            wasted = mx*(i+1)-sm
            dp.append(wasted)
        
        for ops in range(k):
            for j in range(n-1,-1,-1):
                area = 0
                mxh = 0
                for i in range(j,-1,-1):
                    area += nums[i]
                    mxh = max(mxh, nums[i])
                    dp[j+1] = min(dp[j+1],dp[i]+mxh*(j-i+1)-area)
        return dp[n]