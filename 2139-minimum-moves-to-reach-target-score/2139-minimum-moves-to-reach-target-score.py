class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        doubles = 0
        while target>1:
            if doubles==maxDoubles:
                return steps+target-1
            if target%2==1:
                target-=1
            else:
                target//=2
                doubles+=1
            steps+=1
        return steps