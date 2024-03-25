class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = []
        for i,num in enumerate(nums):
            if num==1: ones.append(i)
        n = len(ones)
        median = (k-1)//2 #convention picks left median
        #the general tactic is to first go to median, then return to order-preserving consecutive positions
        left = right = 0
        saves = 0
        for i in range(k):
            if i<median:
                left += ones[median]-ones[i] 
                saves += median-i
            else:
                right += ones[i]-ones[median]
                saves += i-median
        moves = left+right
        for i in range(1,n-k+1):
            median += 1
            left -= ones[median-1]-ones[i-1]
            left += ((k-1)//2)*(ones[median]-ones[median-1])
            right -= (k//2)*(ones[median]-ones[median-1])
            right += ones[i+k-1]-ones[median] 
            moves = min(moves, left+right)
        return moves-saves