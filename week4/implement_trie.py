class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        trav = self.root
        for letter in word:
            if letter not in trav.children:
                trav.children[letter] = Node()
            trav = trav.children[letter]
        trav.end = True


    def search(self, word: str) -> bool:
        trav = self.root
        for letter in word:
            if letter not in trav.children:
                return False
            trav = trav.children[letter]
        return trav.end
        

    def startsWith(self, prefix: str) -> bool:
        trav = self.root
        for letter in prefix:
            if letter not in trav.children:
                return False
            trav = trav.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
