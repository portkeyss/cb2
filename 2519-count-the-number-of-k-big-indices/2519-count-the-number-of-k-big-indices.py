from sortedcontainers import SortedList
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)
        A = SortedList()
        B = SortedList(nums)
        ans = 0
        for x in nums:
            j = A.bisect_left(x)
            A.add(x)
            B.remove(x)
            l = B.bisect_left(x)
            ans += j>=k and l>=k
        return ans    