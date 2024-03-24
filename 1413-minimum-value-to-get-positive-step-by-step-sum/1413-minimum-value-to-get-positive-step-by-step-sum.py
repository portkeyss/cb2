class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        m = 0
        for n in nums:
            s += n
            m = min(m, s)
        return max(1,1-m)