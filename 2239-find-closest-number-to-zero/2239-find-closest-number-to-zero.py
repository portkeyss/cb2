class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dist = ans = inf
        for num in nums:
            if abs(num)<dist:
                dist = abs(num)
                ans = num
            elif abs(num)==dist:
                if num>ans:
                    ans = num
        return ans