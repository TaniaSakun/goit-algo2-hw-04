from trie_handler import TrieHandler

def main():
    handler = TrieHandler()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        handler.trie.put(word, i)

    print("Words with suffix 'e':", handler.count_words_with_suffix("e"))  # apple
    print("Has prefix 'app':", handler.has_prefix("app"))  # True
    
    strings = ["flower", "flow", "flight"]
    print("Longest common prefix:", handler.find_longest_common_prefix(strings)) 

if __name__ == "__main__":
    main()