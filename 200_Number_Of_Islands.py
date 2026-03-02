from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x, y, grid):

            grid[y][x] = 0

            if x != 0:
                if grid[y][x - 1] == "1":
                    dfs[x - 1, y, grid]
            
            if x != len(grid[y]) - 1:
                if grid[y][x + 1] == "1":
                    dfs[x + 1, y, grid]

            if y != 0:
                if grid[y - 1][x] == "1":
                    dfs[x, y - 1, grid]
            
            if y != len(grid) - 1:
                if grid[y + 1][x] == "1":
                    dfs[x, y + 1, grid]


        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    dfs(x, y, grid)
                    count += 1
        
        return count
        
                
            