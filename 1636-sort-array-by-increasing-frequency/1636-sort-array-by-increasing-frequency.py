class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        counter = [(freq, -num) for num, freq in counter.items()]
        counter.sort()
        res = []
        for freq, n in counter:
            res.extend([-n]*freq)
        return res