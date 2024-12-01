class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        i = 0
        j = len(arr) - 1

        while i != (len(arr) - 1):

            if i < j:
                if arr[i] == 2 * arr[j] or arr[i] * 2 == arr[j]:
                    return True
                else:
                    j -= 1
            else:
                i += 1
                j = len(arr) - 1
            
        return False