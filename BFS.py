import Queue


# Breadth-first search algorithm
def bfs(graph, start):

    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    q = Queue.Queue()

    distance[start] = 0

    q.put(start)

    while not q.empty():
        vertex = q.get()
        for neighbour in graph[vertex]:
            dist = distance[vertex] + graph[vertex][neighbour]
            if distance[neighbour] == 'inf' or distance[neighbour] > dist:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                q.put(neighbour)

    return distance, parent
