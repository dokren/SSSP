from BFS import *
from DFS import *
from Bellman_Ford import *
from Dijkstra import *
from Topological import *
from graph_gen import *
import time


# Graph is a dict with vertexes for keys and  dict of edges with weights for values
graph = {1: {2: 1, 3: 1},
         2: {3: 1, 4: 1},
         3: {4: 1},
         4: {},
         5: {6: 1},
         6: {3: 1}}


graph = gen_random_graph(500, 0.5)

print "bfs:"
start_time = time.time()
bfs(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))

print "dfs:"
start_time = time.time()
dfs(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))

print "dijkstra:"
start_time = time.time()
dijkstra(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))

print "bellman-ford:"
start_time = time.time()
bellman_ford(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))
