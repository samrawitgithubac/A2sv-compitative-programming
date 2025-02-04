class Solution:
    def maskPII(self, s: str) -> str:
        res = []
        set1 = {'+', '-', '(', ')', ' '}
        hashmap1 = {
            "***-***-": 10,
            "+*-***-***-": 11,
            "+**-***-***-": 12,
            "+***-***-***-": 13
        }

        if s[0].isalpha():
            for i in range(len(s)):
                if s[i] == '@':
                    st = s[:i]
                    res.append(st[0].lower())
                    res.append("*****")
                    res.append(st[-1].lower())   # Fixed index error from st[i-1] to st[-1]
                    sa = (s[i:]).lower()
                    res.append(sa)
            return "".join(res)
        else:
            s = list(s)
            # Fixed the pop issue: using list comprehension instead of modifying while iterating
            s = [char for char in s if char not in set1]

            number = []
            for i in hashmap1:
                if len(s) == hashmap1[i]:
                    number.append(i)
                    number.append("".join(s[-4:]))  # Fixed to join the last 4 digits as string
            return "".join(number)

        
