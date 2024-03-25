class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        dr = 1
        if homePos[0]<startPos[0]:
            dr = -1
        elif homePos[0]==startPos[0]:
            dr = 0
        
        dc = 1
        if homePos[1]<startPos[1]:
            dc = -1
        elif homePos[1]==startPos[1]:
            dc = 0
        
        res = 0
        if dr!=0:
            res += sum(rowCosts[homePos[0]:startPos[0]:-dr])
        if dc!=0:
            res += sum(colCosts[homePos[1]:startPos[1]:-dc])
        return res