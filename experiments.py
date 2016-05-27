import random
from BFS import *
from DFS import *
from Bellman_Ford import *
from Dijkstra import *
from Topological import *
from graph_gen import *
import time


def exp_all():
    graph = gen_random_graph(100, 0.8, 100)

    start = random.choice(graph.keys())

    print start

    print "bfs:"
    start_time = time.time()
    bfs(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "dfs:"
    start_time = time.time()
    dfs(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    # print "bellman_ford:"
    # start_time = time.time()
    # bellman_ford(graph, 1)
    # print("--- %s seconds ---" % (time.time() - start_time))

    print "dijkstra_list:"
    start_time = time.time()
    dijkstra_list(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "dijkstra_bheap:"
    start_time = time.time()
    dijkstra_bh(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "dijkstra_fheap:"
    start_time = time.time()
    dijkstra_fh(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))


def exp_topological():
    graph = gen_da_graph(2000, 0.5, 100)

    start = random.choice(graph.keys())

    print "bfs:"
    start_time = time.time()
    bfs(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "dfs:"
    start_time = time.time()
    dfs(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "dijkstra_fheap:"
    start_time = time.time()
    dijkstra_fh(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "topological:"
    start_time = time.time()
    topological(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))


def main():
    exp_topological()


if __name__ == "__main__":
    main()