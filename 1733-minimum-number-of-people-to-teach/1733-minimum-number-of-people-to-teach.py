class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        friends = []
        languages = [set()]+[set(l) for l in languages]
        for u,v in friendships:
            if languages[u]&languages[v]: continue
            friends.append((u,v))
        res = inf
        for l in range(1,n+1):
            a = 0
            tmp = set()
            for u,v in friends:
                if l not in languages[u] and u not in tmp:
                    tmp.add(u)
                    a += 1
                if l not in languages[v] and v not in tmp:
                    tmp.add(v)
                    a += 1
            res = min(res, a)
        return res