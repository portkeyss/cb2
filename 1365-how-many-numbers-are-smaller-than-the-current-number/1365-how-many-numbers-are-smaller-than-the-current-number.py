class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [[] for _ in range(101)]
        for i,n in enumerate(nums):
            count[n].append(i)
        ct = 0
        res = [0]*len(nums)
        for n in range(101):
            for i in count[n]:
                res[i] = ct
            ct += len(count[n])
        return res