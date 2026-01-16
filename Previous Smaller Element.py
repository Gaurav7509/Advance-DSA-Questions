class Solution:
    def prevSmaller(self, arr):
        n = len(arr)
        st = []
        ans = []
        for i in range(n):
            while st and st[-1] >= arr[i]:
                st.pop()
            if not st:
                ans.append(-1)
            else:
                ans.append(st[-1])
            st.append(arr[i])
        return ans
