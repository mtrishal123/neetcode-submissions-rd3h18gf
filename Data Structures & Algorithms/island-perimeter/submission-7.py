class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        def bfs(r, c):
            q = deque([(r, c)])
            perimeter = 0
            visit.add((r, c))
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] == 0:
                        perimeter += 1
                    elif (nx, ny) not in visit:
                        visit.add((nx, ny))
                        q.append((nx, ny))
            return perimeter
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return bfs(r, c)
        return 0