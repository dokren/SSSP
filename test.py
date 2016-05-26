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


graph = gen_random_graph(5000, 0.1)

print "bfs:"
start_time = time.time()
bfs(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))

print "dfs:"
start_time = time.time()
dfs(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))

print "dijkstra_list:"
start_time = time.time()
dijkstra_list(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))

print "dijkstra_bheap:"
start_time = time.time()
dijkstra_bh(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))

print "dijkstra_fheap:"
start_time = time.time()
dijkstra_fh(graph, 1)
print("--- %s seconds ---" % (time.time() - start_time))