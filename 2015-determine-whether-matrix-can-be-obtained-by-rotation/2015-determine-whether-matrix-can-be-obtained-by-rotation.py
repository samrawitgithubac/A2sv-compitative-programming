import copy
class Solution(object):
    def findRotation(self, mat, target):
        answer=[]
        copied_mat=copy.deepcopy(mat)
        while answer!=mat:
            answer=[]
            for i in range(len(target)):
                value=[]
                for j in range(len(target)):
                    value.append(copied_mat[j][i])
                value=value[::-1]
                answer.append(value)
            if answer==target:
                return True 
            copied_mat=answer
        return False