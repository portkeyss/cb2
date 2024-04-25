class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        if beginWord not in wordList: wordList.append(beginWord)
 
        A = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                A[w[:i]+"?"+w[i+1:]].append(w)
        
        neis = defaultdict(list)
        for lst in A.values(): #all entries in lst are adjacent
            for i in range(len(lst)):
                for j in range(i):
                    neis[lst[i]].append(lst[j])
                    neis[lst[j]].append(lst[i])
        
        prev = defaultdict(list)      
        dist = defaultdict(lambda:inf)
        dist[beginWord] = 0
        q = deque([beginWord])
        while q:
            x = q.popleft()
            if x==endWord: break
            for y in neis[x]:
                if dist[y]==inf:
                    q.append(y)
                    dist[y] = dist[x]+1
                    prev[y].append(x)
                elif dist[y]== dist[x]+1:
                    prev[y].append(x)
        
        self.res = []
        self.stack = []
        def generateSeq(x):
            self.stack.append(x)
            if x==beginWord:
                self.res.append(self.stack[::-1])
            else:
                for y in prev[x]:
                    generateSeq(y)
            self.stack.pop()
        generateSeq(endWord)
        return self.res