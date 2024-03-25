class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        cur = 0
        for num in nums:
            if num==0 or num==cur: continue
            count += 1
            cur = num
        return count