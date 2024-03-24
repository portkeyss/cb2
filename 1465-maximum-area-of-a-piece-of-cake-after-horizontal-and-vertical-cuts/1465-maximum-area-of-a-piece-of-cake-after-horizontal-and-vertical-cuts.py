class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHSep = horizontalCuts[0]
        
        for i in range(1,len(horizontalCuts)):
            maxHSep = max(maxHSep, horizontalCuts[i] - horizontalCuts[i-1])
        maxHSep = max(maxHSep, h - horizontalCuts[-1])
        
        maxVSep = verticalCuts[0]
        for i in range(1,len(verticalCuts)):
            maxVSep = max(maxVSep, verticalCuts[i] - verticalCuts[i-1])
        maxVSep = max(maxVSep, w - verticalCuts[-1])
        
        return (maxHSep * maxVSep) % (10**9+7)