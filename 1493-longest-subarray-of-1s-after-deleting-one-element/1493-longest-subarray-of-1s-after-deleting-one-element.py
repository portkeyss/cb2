class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #find the longest window with at most one zero
        zeros = 0
        i = 0
        j = 0
        n = len(nums)
        res = 0
        while j < n:
            if nums[j] == 0:
                zeros += 1
            while zeros > 1:
                if nums[i] == 0: 
                    zeros -= 1
                i += 1
            res = max(res, j-i)
            j += 1
        return res