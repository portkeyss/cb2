class Solution:
    def minimumTime(self, s: str) -> int:
        #inspired by a forum post
        arr = [1 if c=="1" else -1 for c in s]
        minSum = curSum = 0
        for x in arr:
            if curSum+x<0:
                curSum += x
                minSum = min(minSum, curSum)
            else:
                curSum = 0
        return len(s)+minSum