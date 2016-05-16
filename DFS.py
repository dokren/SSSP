# Depth-first search
def dfs(graph, start):

    # distances and parents init
    distances = ['inf'] * len(graph)
    parents = ['nil'] * len(graph)

    stack = []

    distances[start - 1] = 0

    stack.append(start)

    while not stack == []:
        vertex = stack.pop()
        for neighbour in graph[vertex]:
            dist = distances[vertex - 1] + neighbour[1]
            if distances[neighbour[0] - 1] == 'inf' or distances[neighbour[0] - 1] > dist:
                distances[neighbour[0] - 1] = dist
                parents[neighbour[0] - 1] = vertex
                stack.append(neighbour[0])

    return distances, parents