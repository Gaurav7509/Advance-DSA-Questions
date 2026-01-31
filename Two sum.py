Pseudocode bruteforce:
for (i=0 to n)
  first = arr[i]
  for (j= i + 1 to n)
    second = arr[j]
    sum = first + second
    if (sum == target)
        return first , second

Code:

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, j in enumerate(nums):
            k = target - j
            if k in num_map:
                return [num_map[k], i]
            num_map[j] = i
        
