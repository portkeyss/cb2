class TrieNode:
     
    def __init__(self, count=0):
        self.count = count
        self.children = defaultdict(TrieNode)
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
        node.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            if c not in node.children: return 0
            node = node.children[c]
        return node.count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children: return 0
            node = node.children[c]
        
        def dfs(tn):
            if len(tn.children)==0: 
                return tn.count
            res = tn.count
            for c,child in tn.children.items():
                res += dfs(child)
            return res
        return dfs(node)

    def erase(self, word: str) -> None:
        def f(idx,parent):
            node = parent.children[word[idx]]
            if idx==len(word)-1:
                node.count -= 1
            else:
                f(idx+1,node)
            if node.count==0 and len(node.children)==0:
                parent.children.pop(word[idx])              
        f(0,self.root)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)