class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefixIdx = dict()
        prefixIdx[0] = -1
        front = -1
        cur = 0
        count = 0
        for i in range(n):
            cur += nums[i]
            if cur-target in prefixIdx:
                j = prefixIdx[cur-target]
                if front<=j:
                    count += 1
                    front = i
            prefixIdx[cur] = i
        return count    