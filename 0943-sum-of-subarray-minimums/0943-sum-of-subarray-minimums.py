from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
       
        pre = [1] * n
        back = [1] * n
        
      
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            pre[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        
       
        stack = []
        
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            back[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        
       
        res = sum(arr[i] * pre[i] * back[i] for i in range(n)) % MOD
        return res
