def bfs_iterative(adj, queue, is_visited, result):
    if not queue:
        return
    node = queue.pop(0)
    result.append(node)
    for i in adj[node]:
        if not is_visited[i]:
            is_visited[i] = True
            queue.append(i)
    bfs_iterative(adj, queue, is_visited, result)
def bfs(edges):
    x = 0
    for u, v in edges:
        x = max(x, u, v)
    adj = [[] for _ in range(x + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    V = len(adj)
    is_visited = [False] * V
    result = []
    for i in range(V):
        if not is_visited[i]:
            is_visited[i] = True
            bfs_iterative(adj, [i],is_visited, result)

    return result


edges = [[0,1],[0,2],[1,2],[2,3],[4,5],[4,6]]
print(*bfs(edges))
