class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList: return []
        if beginWord not in wordList: wordList.append(beginWord)
 
        def adj(a,b):
            return sum(x==y for x,y in zip(a,b))==len(a)-1
        
        prev = defaultdict(list)
        neis = defaultdict(list)
        n = len(wordList)
        for i in range(n):
            for j in range(i+1,n):
                if adj(wordList[i],wordList[j]):
                    neis[wordList[i]].append(wordList[j])
                    neis[wordList[j]].append(wordList[i])
                
        dist = defaultdict(lambda:inf)
        dist[beginWord] = 0
        q = deque([beginWord])
        while q:
            x = q.popleft()
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