class Node:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word):
        cur=self.root
        for w in word:
            if w not in cur.children:
                cur.children[w]=Node()
            cur=cur.children[w]
        cur.is_end=True
        
    def search(self, word):
        cur=self.root
        for w in word:
            if w not in cur.children:
                return False
            cur =cur.children[w]
        return cur.is_end
         
    def startsWith(self, prefix):
        cur=self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur =cur.children[w]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)