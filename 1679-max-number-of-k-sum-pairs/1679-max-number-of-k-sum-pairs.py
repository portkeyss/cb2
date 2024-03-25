class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for x,y in counter.items():
            if k-x in counter: ans += min(y, counter[k-x])
        return ans//2