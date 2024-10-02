class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            # If stack is not empty and the top element is the same as the current character
            if stack and stack[-1] == char:
                stack.pop()  # Remove the last character (duplicate)
            else:
                stack.append(char)  # Add the character to the stack if no duplicate
        return ''.join(stack)  # Return the final result as a string
