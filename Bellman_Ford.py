# Bellman-Ford algorithm
def bellman_ford(graph, start):

    # distances and parents init
    distance = {}
    parent = {}
    for node in graph:
        distance[node] = 'inf'
        parent[node] = 'nil'

    distance[start] = 0

    for i in range(len(graph)-1):
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
