class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(firstname,path):
            if len(path)==k:
                ans.append(path[:])
                return 

            for candidates  in range(firstname,n+1):
                path.append(candidates)
                backtrack(candidates+1 ,path)
                path.pop()
        backtrack(1,[])
        return ans
        

            
        
                
