class Trie:
    def __init__(self):
        self.root = None
        self.d = {}
        # for i in range(ord('a'), ord('z')+1):
        #     self.d[chr(i)] = None

    def insert(self, word):
        if not word[0] in self.d:
            self.d[word[0]] = TrieNode()
        self.d[word[0]].insert(word)

    def printTree(self, char):
        if not char:
            return
        self.d[char].printTree()

class TrieNode:
    def __init__(self):
        self.char = None
        self.d = {}

    def insert(self, word):
        if len(word) > 0 and word[0] not in self.d:
            self.d[word[0]] = TrieNode()
            self.char = word[0]
        if len(word) > 0:
            self.d[word[0]].insert(word[1:len(word)])

    def printTree(self):
        if not self.char:
            return
        print(self.char)
        print(self.d)
        for c in self.d:
            self.d[c].printTree()

if __name__ == '__main__':
    t = Trie()
    t.insert('swap')
    t.insert('sweet')
    t.printTree('s')
