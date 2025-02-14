class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        counter_t = Counter(t)
        window = Counter()

        def check(first, second):
            for char in second:
                if first[char] < second[char]:
                    return False
            
            return True

        left = 0
        right = 0
        ans = float("inf")
        indexes = []

        while right < m:
            window[s[right]] += 1

            while (right-left)+1 >= n and check(window, counter_t):
                current_length = (right-left)+1
                if current_length < ans:
                    ans = current_length
                    indexes = [left, right]
                
                window[s[left]] -= 1
                left += 1

            right += 1
        
        if ans == float("inf"):
            return ""
        
        return s[indexes[0]: indexes[1]+1]
