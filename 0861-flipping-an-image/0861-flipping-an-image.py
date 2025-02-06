class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in range(len(image)):
            Horizontallychanged=image[i]
            res.append(Horizontallychanged[::-1])
        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j]==0:
                    res[i][j]=1
                else:
                    res[i][j]=0
        return res



        