class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        dic =  {}
        index = 0
        if len(haystack) == len(needle) and haystack == needle:
            return 0
        while index + len(needle) <= len(haystack):
            n_gram = haystack[index:index+len(needle)]
            if n_gram not in dic:
                dic[n_gram] = index
            else:
                pass
            index += 1
        if needle in dic:
            return dic[needle]
        return -1
        