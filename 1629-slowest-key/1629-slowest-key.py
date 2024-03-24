class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        duration = defaultdict(lambda:0)
        duration[keysPressed[0]] = releaseTimes[0]
        for i in range(1,len(releaseTimes)):
            c = keysPressed[i]
            d = releaseTimes[i]-releaseTimes[i-1]
            if duration[c] < d:
                duration[c] = d
        dur = [[t, ch] for ch, t in duration.items()]
        dur.sort()
        return dur[-1][-1]