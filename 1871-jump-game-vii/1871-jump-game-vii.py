class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        prefix = [0,1] #how many reachable points are there from start to current index point
        for i in range(1,n):
            inc = 0
            if s[i]=="0" and i>=minJump and prefix[i-minJump+1]-prefix[max(0,i-maxJump)]>0:
                inc = 1
            prefix.append(prefix[-1]+inc)
        return prefix[n]-prefix[n-1]>0 