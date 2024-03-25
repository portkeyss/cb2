class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        ab = [(a,b) for a,b in zip(aliceValues,bobValues)]
        ab.sort(key=lambda x:x[0]+x[1])
        n = len(ab)
        x = y = 0
        flag = True
        for i in range(n-1,-1,-1):
            if flag: x += ab[i][0]
            else: y += ab[i][1]
            flag = not flag
        if x<y: return -1
        if x==y: return 0
        return 1