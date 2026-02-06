class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = n
        m = 0
        
        for i in range(len(nums)):
            while m < n and nums[m] <= nums[i]* k:
                m = m + 1
        
            ans = min(ans, n-(m-i))
        return ans

        
