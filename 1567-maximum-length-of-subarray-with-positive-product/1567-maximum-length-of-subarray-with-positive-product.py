class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        start = 0
        while start < len(nums):
            if nums[start] == 0:
                start += 1
                continue
            end = start
            negative = 0
            while end < len(nums) and nums[end] != 0:
                if nums[end] < 0: negative += 1
                end += 1
            if negative % 2 == 0:
                res = max(res, end-start)
            else: # must split [start,end) with a negative entry
                negCount = 0
                for i in range(start, end):
                    if nums[i] < 0:
                        if negCount%2 == 0:
                            res = max(res, i-start, end-i-1)
                        negCount += 1
            start = end
        return res