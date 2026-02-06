class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentsum = nums[0]
        maxsum = nums[0]
        if not nums:
            return 0 
        for i in range(1, len(nums)):
            num = nums[i]
            currentsum = max(num, currentsum + num)
            maxsum = max(maxsum, currentsum)
            
        return maxsum
