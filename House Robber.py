class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = curr = 0
        for x in nums:
            prev, curr = curr, max(curr, prev + x)
        return curr
