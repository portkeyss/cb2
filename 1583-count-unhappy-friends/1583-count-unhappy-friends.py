class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0]*n for _ in range(n)]
        for i in range(n):
            rank[i][i] = n-1
            for j in range(n-1):
                rank[i][preferences[i][j]] = j
        friend = [0]*n
        for a,b in pairs:
            friend[a]=b
            friend[b]=a
        res = 0
        for i in range(n):
            for j in range(n):
                if i!=j and rank[i][j]<rank[i][friend[i]] and rank[j][i]<rank[j][friend[j]]:
                    res += 1
                    break
        return res