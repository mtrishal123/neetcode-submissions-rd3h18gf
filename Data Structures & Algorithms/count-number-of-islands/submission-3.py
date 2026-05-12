class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        count = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or ny < 0 or nx >= rows or ny >= cols or
                        grid[nx][ny] == "0"):
                        continue
                    visit.add((nx, ny))
                    q.append((nx, ny))
                    grid[nx][ny] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    count += 1
        return count