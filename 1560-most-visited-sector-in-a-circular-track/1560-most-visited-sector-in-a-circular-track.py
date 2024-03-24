class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        rounds = [r-1 for r in rounds]#change to 0-based indexing
        #calculate absolute total distance covered
        s = rounds[0]
        dist = 0
        for e in rounds[1:]:
            dist += (e+n-s)%n
            s = e
        if dist%n==0:
            return [rounds[0]+1]
        a = rounds[0]
        b = (rounds[0]+dist)%n
        return list(range(a+1, b+2)) if a<b else list(range(1,b+2))+list(range(a+1,n+1))