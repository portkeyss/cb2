class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = Counter()
        ans = 0
        for num in nums:
            ans += counter[num-k] + counter[num+k]
            counter[num] += 1
        return ans