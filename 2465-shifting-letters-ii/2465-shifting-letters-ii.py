class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        rangeArr = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            if direction == 1:
                rangeArr[start] += direction
                if end + 1 < len(rangeArr):
                    rangeArr[end + 1] -= direction
            else:
                rangeArr[start] -= 1
                if end + 1 < len(rangeArr):
                    rangeArr[end + 1] += 1
        
        for i in range(1, len(rangeArr)):
            rangeArr[i] += rangeArr[i-1]
        for i in range(len(s)):
            shift = rangeArr[i] % 26  
            rangeArr[i] = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        return "".join(rangeArr[:len(s)])
