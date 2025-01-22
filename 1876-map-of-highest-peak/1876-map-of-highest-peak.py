class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)] 
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]      
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    queue.append((i, j))      
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    queue.append((nx, ny))
        return heights