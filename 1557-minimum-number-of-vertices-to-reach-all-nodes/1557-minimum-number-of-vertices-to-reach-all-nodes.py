class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [0]*n
        for _,x in edges:
            incoming[x] += 1
        return [x for x in range(n) if incoming[x]==0]