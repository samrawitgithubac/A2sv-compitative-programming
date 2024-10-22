class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        arr = []
        for x in range(n):
            arr.append((heights[x], names[x]))
        
        arr.sort(reverse = True)

        for x in range(n):
            names[x] = arr[x][1]
        
        return names
        