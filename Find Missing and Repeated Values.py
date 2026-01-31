class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        s = set()
        n = len(grid)
        actualSum = 0
        repeated = 0
        ans = []
        for i in range(n):
            for j in range(n):
                actualSum += grid[i][j]
                if grid[i][j] in s:
                    repeated = grid[i][j]
                    ans.append(repeated)
                s.add(grid[i][j])
        expSum = (n*n) * (n*n+1) // 2
        missing = expSum + repeated - actualSum
        ans.append(missing)
        return ans
        

