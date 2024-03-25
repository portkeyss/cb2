class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(n*(c==1) for n,c in Counter(nums).items())