# goit-algo2-hw-04
The repository for the 4th GoItNeo Design and Analysis of Algorithms homework

### Task 1: Extending the functionality of the prefix tree
Implement two additional methods for the Trie class:
count_words_with_suffix(pattern) to count the number of words that end with the given pattern;
has_prefix(prefix) to check for the presence of words with the given prefix.

#### Requirements:
- The Homework class must inherit from the base class Trie.

- The methods should handle input errors for incorrect data.

- The input parameters of both methods must be strings.

- The method count_words_with_suffix should return an integer.

- The method has_prefix should return a boolean value.

#### Results:
Input -> ["apple", "application", "banana", "cat"]

Output:
Words with suffix 'e': 1

Has prefix 'app': True

Trie Keys: ['flow', 'flower', 'flight']

### Task 2: Finding the Longest Common Prefix

Create a class LongestCommonWord that inherits from the Trie class, and implement the method find_longest_common_word that finds the longest common prefix for all words in the input array of strings.

#### Requirements:
- The LongestCommonWord class must inherit from Trie.

- The input parameter of the method find_longest_common_word, strings — an array of strings.

- The method find_longest_common_word should return a string — the longest common prefix.

- Execution time — O(S)O(S), where SS is the total length of all strings.

#### Results:
Input -> ['flow', 'flower', 'flight']

Output -> Longest common prefix: fl