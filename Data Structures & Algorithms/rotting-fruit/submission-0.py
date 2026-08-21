class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        step = 0
        queue = deque()
        fresh = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        while queue and fresh:
            step += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))
        return step if fresh == 0 else -1
            
