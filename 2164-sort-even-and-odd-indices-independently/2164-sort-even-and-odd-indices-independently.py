class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in range(len(nums)):
            if i%2==0: evens.append(nums[i])
            else: odds.append(nums[i])
        evens.sort()
        odds.sort(reverse=True)
        evensIter=iter(evens)
        oddsIter=iter(odds)
        res = []
        i = j = 0
        for i in range(len(nums)):
            if i%2==0: res.append(next(evensIter))
            else:res.append(next(oddsIter))
        return res