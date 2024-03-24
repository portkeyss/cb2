class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #this problem is equivalent to find n-k sized subarray that has minimum sum, we use cumulative sum to solve it
        sz = len(cardPoints) - k
        minSum = float('inf')
        cs = [0]
        for i,n in enumerate(cardPoints):
            cs.append(cs[-1] + n)
            if i >= sz - 1: # i has to be at lease the last element of an sz sized array to make legitimate comparison
                minSum = min(minSum, cs[-1] - cs[-1-sz])
        return cs[-1] - minSum
        