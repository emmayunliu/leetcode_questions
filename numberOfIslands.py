class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.helper(grid, row, col)
        return count
                
    def helper(self, grid, row, col):
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.helper(grid, row+1, col)
        self.helper(grid, row, col+1)
        self.helper(grid, row-1, col)
        self.helper(grid, row, col-1)
        
        
        
        
obj = Solution()
print obj.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])