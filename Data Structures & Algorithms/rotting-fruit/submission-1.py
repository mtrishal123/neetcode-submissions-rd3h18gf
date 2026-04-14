class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()

        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    que.append([r, c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while que and fresh > 0:
            for _ in range(len(que)):
                r, c = que.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row == len(grid) or 
                    col == len(grid[0]) or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    que.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1