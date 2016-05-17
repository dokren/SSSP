import Queue
import sys


# Dijkstra algorithm
def dijkstra(graph, start):

    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    q = Queue.PriorityQueue()

    distance[start] = 0

    q.put((1, start))

    while not q.empty():
        tup = q.get()
        vertex = tup[1]
        if distance[vertex] > tup[0]:
            continue
        for neighbour in graph[vertex]:
            dist = distance[vertex] + graph[vertex][neighbour]
            if distance[neighbour] == 'inf' or dist < distance[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                q.put((dist, neighbour))

    return distance, parent
