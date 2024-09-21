class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Initialize the last occurrence of 'a', 'b', and 'c' to -1
        last_a = last_b = last_c = -1
        result = 0  # To store the number of valid substrings

        # Iterate through the string
        for i, char in enumerate(s):
            # Update the last occurrence of the current character
            if char == 'a':
                last_a = i
            elif char == 'b':
                last_b = i
            elif char == 'c':
                last_c = i

            # Calculate the earliest last occurrence of 'a', 'b', and 'c'
            # The earliest one determines the start of the valid substring range
            earliest_last_occurrence = min(last_a, last_b, last_c)

            # If all characters have been seen at least once, add the count
            # of valid substrings ending at this position
            if earliest_last_occurrence != -1:
                result += earliest_last_occurrence + 1

        return result


        