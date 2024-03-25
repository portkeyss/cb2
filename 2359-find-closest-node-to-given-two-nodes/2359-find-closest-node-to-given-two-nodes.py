class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dist(nd):
            A = dict()
            cur = 0
            node = nd
            while node!=-1 and node not in A:
                A[node] = cur
                node = edges[node]
                cur += 1
            return A
        
        d1,d2 = dist(node1), dist(node2)
        j,x = -1,inf
        for nd in d1:
            if nd in d2:
                y = max(d1[nd],d2[nd])
                if y<x or y==x and nd<j:
                    j,x = nd,y
        return j