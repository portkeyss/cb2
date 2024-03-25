class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userTime = defaultdict(set)
        for id,t in logs:
            userTime[id].add(t)
        res = [0]*k
        for s in userTime.values():
            res[len(s)-1] += 1
        return res