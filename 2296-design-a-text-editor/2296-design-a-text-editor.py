class Node:
    def __init__(self,_val):
        self.val = _val
        self.prev = None
        self.next = None
        
class TextEditor:
    #double linked list
    def __init__(self):
        self.cur = Node(" ")

    def addText(self, text: str) -> None:
        s = self.cur.next
        for ch in text:
            nd = Node(ch)
            nd.prev = self.cur
            self.cur.next = nd
            self.cur = nd
        self.cur.next = s
        if s: s.prev = self.cur

    def deleteText(self, k: int) -> int:
        count = 0
        s = self.cur.next
        while count<k and self.cur.val!=" ":
            x = self.cur
            self.cur = self.cur.prev
            del x
            count += 1
        self.cur.next = s
        if s: s.prev = self.cur
        return count
    
    def helper(self):
        buffer = []
        t = self.cur
        p = 10
        while p>0 and t and t.val!=" ":
            buffer.append(t.val)
            t = t.prev
            p -= 1
        return "".join(buffer[::-1])
        
    def cursorLeft(self, k: int) -> str:
        while k>0 and self.cur.val!=" ":
            self.cur = self.cur.prev
            k -= 1  
        return self.helper()

    def cursorRight(self, k: int) -> str:
        while k>0 and self.cur.next:
            self.cur = self.cur.next
            k -= 1
        return self.helper()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)