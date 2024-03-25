class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        s = set(nums[0])
        for array in nums[1:]:
            s &= set(array)
        return sorted(list(s))