import numpy as np


# Bellman-Ford algorithm
def bellman_ford1(graph, start):
    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    distance[start] = 0

    for i in range(len(graph) - 1):
        changes = False
        for v in graph:
            if not distance[v] == 'inf':
                for n in graph[v]:
                    if distance[n] == 'inf' or distance[n] > distance[v] + graph[v][n]:
                        changes = True
                        distance[n] = distance[v] + graph[v][n]
                        parent[n] = v

        if not changes:
            break

    return distance, parent


def bellman_ford2(graph, start):
    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    distance[start] = 0

    c = set()
    c.add(start)

    while c:
        changed = set()
        for v in graph:
            if v in c or v in changed:
                if v in changed:
                    changed.remove(v)
                for n in graph[v]:
                    if distance[n] == 'inf' or distance[n] > distance[v] + graph[v][n]:
                        distance[n] = distance[v] + graph[v][n]
                        parent[n] = v
                        changed.add(n)

        c = set(changed)

    return distance, parent


def bellman_ford3(graph, start):
    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    distance[start] = 0

    order = list(graph)
    order = list(np.random.permutation(order))

    index = order.index(start)
    temp = order[index]
    order[index] = order[0]
    order[0] = temp

    r_order = list(order)
    r_order.reverse()

    graph_plus = dict()
    graph_minus = dict()

    for v in graph:
        neighbours_p = dict()
        for e in graph[v]:
            if order.index(e) > order.index(v):
                neighbours_p[e] = graph[v][e]
        graph_plus[v] = neighbours_p

    for v in graph:
        neighbours_m = dict()
        for e in graph[v]:
            if order.index(e) < order.index(v):
                neighbours_m[e] = graph[v][e]
        graph_minus[v] = neighbours_m

    c = set()
    c.add(start)

    while c:
        changed = set()
        for v in order:
            if v in c or v in changed:
                for n in graph_plus[v]:
                    if distance[n] == 'inf' or distance[n] > distance[v] + graph_plus[v][n]:
                        distance[n] = distance[v] + graph_plus[v][n]
                        parent[n] = v
                        changed.add(n)

        for v in r_order:
            if v in c or v in changed:
                for n in graph_minus[v]:
                    if distance[n] == 'inf' or distance[n] > distance[v] + graph_minus[v][n]:
                        distance[n] = distance[v] + graph_minus[v][n]
                        parent[n] = v
                        changed.add(n)

        c = set(changed)

    return distance, parent
