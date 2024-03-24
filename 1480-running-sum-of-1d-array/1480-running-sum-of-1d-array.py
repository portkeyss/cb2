class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        res = []
        for num in nums:
            s += num
            res.append(s)
        return res