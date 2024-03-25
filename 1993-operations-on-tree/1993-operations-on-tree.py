class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.children = [[] for _ in range(n)]
        for c,p in enumerate(parent):
            if p!=-1:  self.children[p].append(c)
        self.locker = [-1]*n

    def lock(self, num: int, user: int) -> bool:
        if self.locker[num]==-1:
            self.locker[num] = user
            return True
        else:
            return False
            
    def unlock(self, num: int, user: int) -> bool:
        if self.locker[num]==user:
            self.locker[num] = -1
            return True
        else:
            return False
            
    def upgrade(self, num: int, user: int) -> bool:
        node = num
        while node!=-1 and self.locker[node]==-1:
            node = self.parent[node]
        if node != -1: return False
        q = deque([num])
        A = []
        while q:
            node = q.popleft()
            for c in self.children[node]:
                if self.locker[c]!=-1: A.append(c)
                q.append(c)
        if not A: return False
        for node in A:
            self.locker[node] = -1
        self.locker[num] = user
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)