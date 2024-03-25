class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        ones = numCount[1]
        if 1 in numCount: numCount.pop(1)
        forbidden = [4,8,9,12,16,18,20,24,25,27,28] #numbers that have multiple same prime counts
        for num in forbidden:
            if num in numCount:
                numCount.pop(num)
        uniqueNums = list(numCount.keys())
        n = len(uniqueNums)
        primes = [2,3,5,7,11,13,17,19,23,29]
        primeFactors = [0]*n #prime factors of a given number expressed in bit form
        for i in range(n):
            for j in range(len(primes)):
                if uniqueNums[i]%primes[j]==0:
                    primeFactors[i] |= 1<<j
        
        def f(i,existingPrimes):
            if i==n: return 1
            currentPrimes = primeFactors[i]
            ans = f(i+1, existingPrimes)
            if currentPrimes&existingPrimes==0:
                ans += numCount[uniqueNums[i]]*f(i+1,existingPrimes|currentPrimes)
            return ans
        
        res = 2**ones*(f(0,0)-1) #-1 means getting rid of empty set
        return res%(10**9+7)