class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert_string(bits):
            bits = list(bits)
            for i in range(len(bits)):
                if bits[i] == "0":
                    bits[i] = "1"
                else:
                    bits[i] = "0"
            return "".join(bits)
        def reverse_string(bits):
           return bits[::-1]
        def concatination(n):
            if n == 1:
                return "0"
            return concatination(n-1) + "1" + reverse_string(invert_string(concatination(n-1)))
       
        binary = concatination(n)
        return binary[k-1]
