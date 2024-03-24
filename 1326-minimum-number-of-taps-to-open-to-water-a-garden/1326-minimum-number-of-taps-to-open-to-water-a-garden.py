class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = {}
        for i,a in enumerate(ranges):
            if a == 0: continue
            s = max(0, i-a)
            e = min(n, i+a)
            if s not in intervals or intervals[s] < e:
                intervals[s] = e
        intervals = [(s,e) for s,e in intervals.items()]
        intervals.sort()
        
        front = 0
        ans = 0
        i = 0
        while front < n:
            nextFront = front
            while i < len(intervals) and intervals[i][0] <= front:
                nextFront = max(nextFront, intervals[i][1])
                i += 1
            if nextFront > front:                
                front = nextFront
                ans += 1
            else:
                return -1         
        return ans