class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = 0
        diff = 0
        diff2Idx = {0:-1}
        ans = 0
        for i,x in enumerate(nums):
            s = s + (1 if x==1 else -1)
            if s in diff2Idx: ans = max(ans, i-diff2Idx[s])
            else: diff2Idx[s] = i
        return ans