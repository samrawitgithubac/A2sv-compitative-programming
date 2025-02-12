class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        noOfteam=len(skill)//2
        i=0
        j=len(skill)-1
        res=[]
        ans=0
        chemistry=[]
        while i<j:
            chemistry.append((skill[i],skill[j]))
            i+=1
            j-=1
        print(chemistry)
        for i in  chemistry:
            s1=i[0]+i[1]
            res.append(s1)
        if len(set(res))==1:
            for  i in chemistry:
                ans+=(i[0]*i[1])
            return ans
        else:
            return -1
        


            



        




        