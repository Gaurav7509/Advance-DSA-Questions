class Solution:
    def activitySelection(self, start, finish):
        #code here
        meetings = []
        n = len(start)
        for i in range(n):
            meetings.append((finish[i],start[i]))
        meetings.sort()
        count = 0
        end = -1
        
        for f ,s in meetings:
            
            if s > end:
                count = count + 1
                end = f
        return count
        
