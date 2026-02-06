class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nums = prices
        minprice = nums[0]
        profit = 0
        for i in range(1 , len(nums)):
            if nums[i] < minprice:
                minprice = nums[i]
            elif nums[i] - minprice > profit:
                profit = nums[i] - minprice
        return profit
