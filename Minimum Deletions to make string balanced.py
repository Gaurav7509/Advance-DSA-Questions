class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = 0
        ans = 0
        for i in s:
            if i == "b":
                b = b + 1
            else:
                ans = ans + 1
                ans = min(ans ,b)

        return ans 


        
