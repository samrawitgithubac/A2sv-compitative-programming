class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[[1]]
        for i in range(1,rowIndex+1):
            row=[1]
            rowlast=res[-1]
            for  j in range(1,len(rowlast)):
                row.append(rowlast[j-1]+rowlast[j])
            row.append(1)
            res.append(row)

        return res[-1]

        