class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0,0))
        cur = [0,0]
        for p in path:
            if p=="N": 
                cur[0]-=1
            elif p=="S":
                cur[0]+=1
            elif p=="E":
                cur[1]+=1
            else:
                cur[1]-=1
            if tuple(cur) in visited: return True
            visited.add(tuple(cur))
        return False