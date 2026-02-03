class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 1
        while i < n and nums[i] > nums[i-1]:
            i = i + 1
        if i == 1 or i == n:
            return False

        p = i - 1


        while i < n and nums[i] < nums[i-1]:
            i = i + 1
        if i == p + 1 or i == n:
            return False

        q = i - 1


        while i < n and nums[i] > nums[i-1] : 
            i = i+1
        return i == n
