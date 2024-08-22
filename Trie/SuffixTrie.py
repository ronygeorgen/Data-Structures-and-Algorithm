class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.ref_count = 0

class SuffixTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        for i in range(len(word)):
            self._insert_suffix(word[i:])
        
    def _insert_suffix(self, suffix):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.ref_count += 1
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, suffix):
        node = self.root
        stack = []
        for char in suffix:
            if char not in node.children:
                return False  # Suffix not in trie, nothing to delete
            stack.append((node, char))
            node = node.children[char]
        
        if not node.is_end:
            return False  # Word is not marked as a complete word
        
        # Unmark the word
        node.is_end = False
        
        # Remove nodes if they're no longer needed
        for parent, char in reversed(stack):
            node.ref_count -= 1
            if node.ref_count == 0:
                del parent.children[char]
            node = parent
        
        return True

trie = SuffixTrie()
word = "banana"
trie.insert(word)
print(trie.delete("as"))  # Should print False
print(trie.search("banana"))  # True
print(trie.search("ana"))  # True
print(trie.search("ban"))  # False
print(trie.search("na"))  # True
print(trie.search("a"))  # True
print(trie.search("n"))  # False
print(trie.search("bs"))  # False
print(trie.search("anana"))  # True
print(trie.search("nana"))  # True
print(trie.search("ananaa"))  # False

# Additional tests
print(trie.delete("ana"))  # Should print True
print(trie.search("ana"))  # Should now print False
print(trie.search("na"))  # Should still print True
print(trie.delete("banana"))  # Should print True
print(trie.search("banana"))  # Should now print False