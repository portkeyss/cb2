class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        if n==1: return target[0]==1
        pq = [-x for x in target]
        heapq.heapify(pq)
        s = sum(target)
        while -pq[0]>1:
            a = -heapq.heappop(pq)
            if s-a==1: return True
            if a<s-a: return False
            b = a%(s-a)
            if b==0: return False
            heapq.heappush(pq,-b)
            s = s-a+b
        return True