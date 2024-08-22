class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.ref_count = 0

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
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

    def delete(self, word):
        node = self.root
        stack = []
        for char in word:
            if char not in node.children:
                return False  # Word not in trie, nothing to delete
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
    
    def prefix_search_suggestion(self, prefix):
        mylist = []
        node = self.root

        # Traverse through the prefix
        for char in prefix:
            if char not in node.children:
                return []  # Prefix not found, return empty list
            node = node.children[char]

        # Helper function to collect all words starting from the current node
        def collect_words(node, current_prefix):
            if node.is_end:
                mylist.append(current_prefix)
            for char, next_node in node.children.items():
                collect_words(next_node, current_prefix + char)

        # Start collecting words from the end of the prefix
        collect_words(node, prefix)

        return mylist



trie = PrefixTrie()
words = ["apple", "app", "apricot", "banana"]
for word in words:
    trie.insert(word)
# print(trie.delete("apple"))
# print(trie.getString("a"))   
# print(trie.search("app"))     
# print(trie.search("apricot")) 
# print(trie.search("ap"))       
# print(trie.starts_with("ap")) 
# print(trie.starts_with("ban"))
print(trie.prefix_search_suggestion("ap")) 