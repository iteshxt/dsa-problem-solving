class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]: return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in [0, n-1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m-1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        trapped = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_height = 0
        while heap:
            h, x, y = heapq.heappop(heap)
            max_height = max(max_height, h)
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    trapped += max(0, max_height - heightMap[nx][ny])
                    heapq.heappush(heap, (heightMap[nx][ny], nx, ny))
        return trapped
