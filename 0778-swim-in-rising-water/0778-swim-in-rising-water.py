class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            t, x, y = heapq.heappop(heap)
            if (x, y) == (n-1, n-1): return t
            if visited[x][y]: continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(heap, (max(t, grid[nx][ny]), nx, ny))
