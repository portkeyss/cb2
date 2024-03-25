class Solution:
    def countNicePairs(self, nums: List[int]) -> int:       
        C = Counter(map(lambda x:x-int(str(x)[::-1]), nums))
        return sum(a*(a-1)//2 for a in C.values())%(10**9+7)    