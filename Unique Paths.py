class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [ [ -1 ] * n for _ in range(m) ]
        def solve(i,j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]

            ans = solve(i+1,j) + solve(i,j+1)
            memo[i][j] = ans
            return ans
        return solve(0,0)
#sol = unique(5,5)
#print(sol)



        #dp = [[1]*n for _ in range(m)]
        #for i in range(1, m):
        #    for j in range(1, n):
        #        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #return dp[m-1][n-1]
