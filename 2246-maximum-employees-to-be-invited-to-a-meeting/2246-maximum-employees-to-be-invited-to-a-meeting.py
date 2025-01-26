from collections import deque

class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        inDegree = [0] * n

        # Calculate in-degrees for all nodes
        for f in favorite:
            inDegree[f] += 1

        # Step 1: Process chains using BFS
        queue = deque([i for i in range(n) if inDegree[i] == 0])
        chainLengths = [0] * n
        while queue:
            node = queue.popleft()
            nextNode = favorite[node]
            chainLengths[nextNode] = max(chainLengths[nextNode], chainLengths[node] + 1)
            inDegree[nextNode] -= 1
            if inDegree[nextNode] == 0:
                queue.append(nextNode)

        # Step 2: Detect cycles and calculate sizes
        visited = [False] * n
        maxCycleSize = 0
        twoCycleChains = 0

        for i in range(n):
            if not visited[i] and inDegree[i] > 0:
                cycleSize = 0
                node = i
                while not visited[node]:
                    visited[node] = True
                    node = favorite[node]
                    cycleSize += 1

                if cycleSize == 2:  # Special case for 2-cycles
                    a, b = i, favorite[i]
                    twoCycleChains += 2 + chainLengths[a] + chainLengths[b]
                else:
                    maxCycleSize = max(maxCycleSize, cycleSize)

        # Step 3: Return the best result
        return max(maxCycleSize, twoCycleChains)