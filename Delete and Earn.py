class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 0
            freq[x] += 1
        arr = []
        for x in freq:
            arr.append(x)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        n = len(arr)
        memo = {}
        def solve(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            take = freq[arr[i]] * arr[i]
            j = i + 1
            if j < n and arr[j] == arr[i] + 1:
                j += 1
            ans = max(take + solve(j), solve(i + 1))
            memo[i] = ans
            return ans

        return solve(0)
