class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, h = 1, max(nums)
        while l < h:
            mid = (l+h)//2
            if sum((num-1)//mid for num in nums) > maxOperations:
                l = mid+1
            else:
                h = mid
        return l