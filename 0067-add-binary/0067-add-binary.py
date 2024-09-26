class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []  # To store the resulting binary sum
        carry = 0  # To track carry during addition
        i, j = len(a) - 1, len(b) - 1  # Pointers starting from the last character of each string
        
        # Iterate while there are still bits to process in either a or b, or there's a carry
        while i >= 0 or j >= 0 or carry:
            # Get the current bit for both strings (or 0 if the string has been exhausted)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate the sum of the bits and the carry
            total = bit_a + bit_b + carry
            
            # Append the result of the current bit (total % 2) to the result list
            result.append(str(total % 2))
            
            # Update the carry (total // 2)
            carry = total // 2
            
            # Move the pointers to the next bits
            i -= 1
            j -= 1
        
        # The result is in reverse order, so reverse it before joining to a string
        return ''.join(result[::-1])

        