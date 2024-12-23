import sys


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if word[: len(searchWord)] == searchWord:
                return i + 1
        return -1


sentence = sys.argv[1]
searchWord = sys.argv[2]

print(Solution().isPrefixOfWord(sentence, searchWord))
