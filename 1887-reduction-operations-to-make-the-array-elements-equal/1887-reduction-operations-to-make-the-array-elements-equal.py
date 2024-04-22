class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        uniques = sorted(count.keys(), reverse=True)
        cummulative = 0
        ops = 0
        for x in uniques[:-1]:
            cummulative += count[x]
            ops += cummulative
        return ops