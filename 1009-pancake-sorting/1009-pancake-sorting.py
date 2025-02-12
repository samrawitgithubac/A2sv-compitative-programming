class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        test = arr
        sort = sorted(arr)
        n = len(arr)
        res = []
        max_ = n-1 # The index were we want to put the max

        while (test != sort):
            max_index = max(range(n), key=arr.__getitem__)
            test[0:max_index+1] = test[0:max_index+1][::-1]
            res.append(max_index+1)
            test[0:max_+1] = test[0:max_+1][::-1]
            res.append(max_+1)
            max_ -=1
            n-=1
        
        return res

        