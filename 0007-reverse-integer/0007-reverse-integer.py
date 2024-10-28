class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        s = []
        q = []

        # Separate the sign and digits
        for i in range(len(y)):
            if not y[i].isdigit():
                s.append(y[i])
            else:
                q.append(y[i])

        # Reverse the digits
        q.reverse()
        s.extend(q)

        # Remove leading zeros
        while len(s) > 1 and s[0] == "0":
            s.pop(0)

        # Join the list to form the result string
        result_str = "".join(s)

        # Check if the result is empty or only a "-" (edge case for -0)
        if result_str == "" or result_str == "-":
            return 0

        # Convert result string to an integer
        result_int = int(result_str)

        # Check for 32-bit integer overflow
        if result_int < -2**31 or result_int > 2**31 - 1:
            return 0

        return result_int
