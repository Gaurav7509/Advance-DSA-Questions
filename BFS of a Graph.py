class Solution:
    def bfs(self, adj):
        length = len(adj)
        visited = [False] * length
        result = []
        order = []    
        index = 0
        order.append(0)
        visited[0] = True
        while index < len(order):
            node = order[index]   
            index += 1            
            result.append(node)
            for i in adj[node]:
                if not visited[i]:
                    visited[i] = True
                    order.append(i)
        return result
