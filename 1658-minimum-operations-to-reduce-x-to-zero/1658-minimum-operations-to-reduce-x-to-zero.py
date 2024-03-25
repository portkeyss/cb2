class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        y = sum(nums)-x
        if y<0: return -1
        if y==0: return n
        prefix2Idx = dict()
        prefix2Idx[0] = -1
        sm = 0
        res = inf
        for i,num in enumerate(nums):
            sm += num
            if sm-y in prefix2Idx:
                res = min(res, n-(i-prefix2Idx[sm-y]))
            prefix2Idx[sm] = i
        return res if res<inf else -1