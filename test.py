from BFS import *
from DFS import *
from Bellman_Ford import *
from Dijkstra import *
from Topological import *


# Graph is a dict with vertexes for keys and  dict of edges with weights for values
graph = {1: {2: 1, 3: 1},
         2: {3: 1, 4: 1},
         3: {4: 1},
         4: {},
         5: {6: 1},
         6: {3: 1}}


print "bfs:"
print bfs(graph, 1)

print "dfs:"
print dfs(graph, 1)

print "bellman-ford:"
print bellman_ford(graph, 1)

print "dijkstra:"
print dijkstra(graph, 1)

print "topological:"
print topological(graph, 1)