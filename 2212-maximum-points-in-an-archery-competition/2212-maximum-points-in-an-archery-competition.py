class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        choice = None
        maxPoints = 0
        for mask in range(1<<12):
            points = 0
            minArrow = 0
            for j in range(12):
                if mask&(1<<j):
                    minArrow += aliceArrows[j]+1
                    points += j
            if points>maxPoints and minArrow<=numArrows:      
                maxPoints = points
                choice = mask
        
        res = []
        minArrows = 0
        for j in range(12):
            if choice&(1<<j):
                res.append(aliceArrows[j]+1)
                minArrows += aliceArrows[j]+1
            else:
                res.append(0)
        res[0] += numArrows-minArrows #extra points can be added to any section
        return res