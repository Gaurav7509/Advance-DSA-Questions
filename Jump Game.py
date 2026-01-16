class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maximum = 0
        
        for i in range(len(nums)):
            if i > maximum:
                return False
            
            if i + nums[i] > maximum:
                maximum = i + nums[i]
        
        return True

