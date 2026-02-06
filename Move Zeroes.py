class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range (len(nums)):
            if nums[i] !=0:
                nums[pos] , nums[i] = nums[i] , nums[pos]
                pos = pos+1

solution = Solution()
nums1 = [0,1,0,3,12]
solution.moveZeroes(nums1)
print(nums1)

nums2 = [0]
solution.moveZeroes(nums2)
print(nums2)
