class Solution:
    def dfs(self, adj):
        V = len(adj)
        is_visited = [False] * V
        result = []
        def dfs_visited(u):
            is_visited[u] = True
            result.append(u)
            for i in adj[u]:
                if not is_visited[i]:
                    dfs_visited(i)
        
        dfs_visited(0)
        return result
