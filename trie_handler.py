from trie import Trie

class TrieHandler:
    def __init__(self):
        self.trie = Trie()

    def count_words_with_suffix(self, pattern):
        def _count_suffix(node, path):
            count = 0
            if node.value is not None and "".join(path).endswith(pattern):
                count += 1
            for char, child in node.children.items():
                path.append(char)
                count += _count_suffix(child, path)
                path.pop()
            return count

        return _count_suffix(self.trie.root, [])

    def has_prefix(self, prefix):
        current = self.trie.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def find_longest_common_prefix(self, strings):
        self.trie = Trie()
        for i, string in enumerate(strings):
            self.trie.put(string, i)

        common_prefix = []
        current = self.trie.root

        while len(current.children) == 1 and current.value is None:
            char, child_node = next(iter(current.children.items()))
            common_prefix.append(char)
            current = child_node

        return "".join(common_prefix)