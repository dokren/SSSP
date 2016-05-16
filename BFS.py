import Queue


# Breadth-first search
def bfs(graph, start):

    # distances and parents init
    distances = ['inf'] * len(graph)
    parents = ['nil'] * len(graph)

    q = Queue.Queue()

    distances[start - 1] = 0

    q.put(start)

    while not q.empty():
        vertex = q.get()
        for neighbour in graph[vertex]:
            dist = distances[vertex - 1] + neighbour[1]
            if distances[neighbour[0] - 1] == 'inf' or distances[neighbour[0] - 1] > dist:
                distances[neighbour[0] - 1] = dist
                parents[neighbour[0] - 1] = vertex
                q.put(neighbour[0])

    return distances, parents
