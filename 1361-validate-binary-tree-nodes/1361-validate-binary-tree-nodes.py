class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = set()
        roots = set()
        q = deque()
        for i in range(n):
            if i not in visited:
                q.append(i)
                visited.add(i)
                while q:
                    node = q.popleft()
                    l, r = leftChild[node], rightChild[node]
                    children = []
                    if l > -1: children.append(l)
                    if r > -1: children.append(r)
                    for c in children:
                        if c in roots:
                            roots.remove(c)
                        elif c in visited:
                            return False
                        else:
                            visited.add(c)
                            q.append(c)
                roots.add(i)
        return len(roots) == 1