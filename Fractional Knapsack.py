class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        n = len(val) 
        items = []
        for i in range(n):
            items.append((val[i]/wt[i],val[i],wt[i]))
        items.sort(reverse= True)
        curr_val = 0.0
        curr_wt = 0
        
        for r , v , w in items:
            
            if curr_wt + w <= capacity:
                curr_wt += w
                curr_val += v
            else:
                remain = capacity - curr_wt
                curr_val += r * remain
                break
        return curr_val
