class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]

        for i in logs:
            if stack and i=='../':
                stack.pop()
            else:
                if i!='../' and i!='./':
                    stack.append(i)
        return len(stack)




                
            

        
        