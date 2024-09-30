class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
      if not grid or not grid[0]:

      return 0
 rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 'L':
                return
            
            # Mark the current land as visited
            grid[i][j] = 'V'
            
            # Explore adjacent cells
            dfs(i+1, j)  # Down
            dfs(i-1, j)  # Up
            dfs(i, j+1)  # Right
            dfs(i, j-1)  # Left
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    dfs(i, j)
                    island_count += 1
        
        return island_count
