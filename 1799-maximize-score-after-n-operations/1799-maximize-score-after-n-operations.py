class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcds = dict()
        for p in range(n-1):
            for q in range(p+1, n):
                gcds[(p,q)] = math.gcd(nums[p], nums[q])
        
        @lru_cache(None)
        def f(i, mask):
            if i == n+1:
                return 0
            ans = 0
            for p in range(n-1):
                for q in range(p+1, n):
                    mask1 = (1<<p) + (1<<q)
                    if not mask&mask1:
                        ans = max(ans, i*gcds[(p,q)]+f(i+1, mask+mask1))
            return ans
 
        return f(1,0)