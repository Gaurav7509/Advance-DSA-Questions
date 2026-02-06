class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        p = 1
        for i in range(n):
            answer[i] = p
            p = p * nums[i]
        s = 1
        for i in range(n-1,-1,-1):
            answer[i] = answer[i]*s
            s = s*nums[i]
        return answer

solution = Solution()
nums1 = [1,2,3,4]
print(solution.productExceptSelf(nums1))
nums2 = [-1,1,0,-3,3]
print(solution.productExceptSelf(nums2))
        
