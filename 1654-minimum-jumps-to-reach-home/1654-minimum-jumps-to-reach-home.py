class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0: return 0
        cap = max([x]+forbidden)+a+b #this is something I don't understand, for pratical purpose, I might use mx to be a very large yet reachable number as the first try
        forbidden = set(forbidden)
        q = deque()
        q.append((0,False)) #first element is position, second being a boolean for backward movement
        dist = dict()
        dist[(0,False)] = 0
        while q:
            y, flag = q.popleft()
            if y+a<= cap and y+a not in forbidden and (y+a,False) not in dist:
                q.append((y+a, False))
                dist[(y+a, False)] = dist[(y,flag)] + 1
                if y+a == x:
                    return dist[(x, False)]
            if flag is False and y-b > 0 and y-b not in forbidden and (y-b, True) not in dist and (y-b, False) not in dist:
                q.append((y-b, True))
                dist[(y-b, True)] = dist[(y,False)] + 1
                if y-b == x:
                    return dist[(x, True)]
        return -1