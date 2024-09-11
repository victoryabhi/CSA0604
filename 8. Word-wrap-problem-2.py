'''
8. Word Wrap Problem
Design a special dictionary that searches the words in it by a prefix and a suffix.
Implement the WordFilter class:
WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
Example 1:
Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".

'''
class WordFilter:
    def __init__(self, words):
        self.words = words
        self.prefix_suffix_map = {}
        
        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                for j in range(len(word) + 1):
                    prefix = word[:i]
                    suffix = word[j:]
                    self.prefix_suffix_map[(prefix, suffix)] = index

    def f(self, pref, suff):
        return self.prefix_suffix_map.get((pref, suff), -1)

wordFilter = WordFilter(["apple"])
print(wordFilter.f("a", "e")) 
