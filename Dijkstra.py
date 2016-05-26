from bheap import *
from fheap import *


# Dijkstra algorithm
def dijkstra_list(graph, start):

    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    alist = []

    distance[start] = 0

    alist.append((1, start))

    while not alist == []:
        minel = min(alist)
        alist.remove(minel)
        tup = minel
        vertex = tup[1]
        if distance[vertex] > tup[0]:
            continue
        for neighbour in graph[vertex]:
            dist = distance[vertex] + graph[vertex][neighbour]
            if distance[neighbour] == 'inf' or dist < distance[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                alist.append((dist, neighbour))

    return distance, parent


def dijkstra_bh(graph, start):

    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    hp = []
    heapmap = dict()

    distance[start] = 0

    heappush(hp, (1, start), heapmap)

    while hp:
        tup = heappop(hp, heapmap)
        vertex = tup[1]
        for neighbour in graph[vertex]:
            dist = distance[vertex] + graph[vertex][neighbour]
            if distance[neighbour] == 'inf' or dist < distance[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                okey = (distance[neighbour], neighbour)
                if okey in heapmap:
                    heapreplace(hp, okey, (dist, neighbour), heapmap)
                else:
                    heappush(hp, (dist, neighbour), heapmap)

    return distance, parent


def dijkstra_fh(graph, start):

    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    hp = Fibonacci_heap()

    distance[start] = 0

    in_queue = dict()

    ent = hp.enqueue(start, 1)
    in_queue[start] = ent

    while hp:
        entry = hp.dequeue_min()
        vertex = entry.get_value()
        dist = entry.get_priority()
        if distance[vertex] > dist:
            continue
        for neighbour in graph[vertex]:
            dist = distance[vertex] + graph[vertex][neighbour]
            if distance[neighbour] == 'inf' or dist < distance[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                if neighbour in in_queue:
                    hp.decrease_key(in_queue[neighbour], dist)
                else:
                    ent = hp.enqueue(neighbour, dist)
                    in_queue[neighbour] = ent

    return distance, parent