class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and iterate backwards
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Set the current digit to 0 and continue to the next iteration
            digits[i] = 0
        
        # If all digits were 9, we'll end up here, so we need to add a new 1 at the beginning
        return [1] + digits

            



        