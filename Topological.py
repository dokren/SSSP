import collections


GRAY, BLACK = 0, 1


# Topological algorithm
def topological(graph, start):

    order = collections.deque()
    enter = set(graph)
    state = {}

    def dfs(root):
        state[root] = GRAY
        for k in graph[root]:
            sk = state.get(k, None)
            if sk == GRAY:
                raise ValueError("cycle")
            if sk == BLACK:
                continue
            enter.discard(k)
            dfs(k)
        order.appendleft(root)
        state[root] = BLACK

    while enter:
        dfs(enter.pop())

    top_order = list(order)

    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    distance[start] = 0

    for vertex in top_order[top_order.index(start):]:
        if distance[vertex] == 'inf':
            continue
        for neighbour in graph[vertex]:
            dist = distance[vertex] + graph[vertex][neighbour]
            if distance[neighbour] == 'inf' or dist < distance[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex

    return distance, parent