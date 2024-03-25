class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        less = 0
        more = 0
        equal = 0
        for k in nums:
            if k<target: less += 1
            elif k>target: more += 1
            else: equal += 1
        if equal==0: return []
        else: return [i for i in range(less, n-more)]