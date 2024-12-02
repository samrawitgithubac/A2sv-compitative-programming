class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        the_list = sentence.split(" ")
        c = 0
        for i in the_list:
            if i.startswith(searchWord):
                return c + 1
            c += 1
        return -1