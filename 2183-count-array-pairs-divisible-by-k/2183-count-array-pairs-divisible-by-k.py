class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def getFactors(x):
            y = 1
            factors = []
            while y*y<x:
                if x%y==0: 
                    factors.append(y)
                    factors.append(x//y)
                y += 1
            if y*y==x:
                factors.append(y)
            return factors
        kFactors = getFactors(k)
        factorCounts = Counter()
        res = 0
        for num in nums:
            minExtraFactor = k//gcd(k,num)
            res += factorCounts[minExtraFactor]
            for f in kFactors:
                if num%f==0:
                    factorCounts[f] += 1
        return res