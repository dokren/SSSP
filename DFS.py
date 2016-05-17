# Depth-first search algorithm
def dfs(graph, start):

    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    stack = []

    distance[start] = 0

    stack.append(start)

    while not stack == []:
        vertex = stack.pop()
        for neighbour in graph[vertex]:
            dist = distance[vertex] + graph[vertex][neighbour]
            if distance[neighbour] == 'inf' or distance[neighbour] > dist:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                stack.append(neighbour)

    return distance, parent