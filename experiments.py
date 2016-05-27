import random
from BFS import *
from DFS import *
from Bellman_Ford import *
from Dijkstra import *
from Topological import *
from graph_gen import *
import time


def exp_random_graph(prob, weight_range):
    f = open('test_results/random_g.txt', 'w+')
    for nodes in range(100, 501, 100):
        for i in range(10):
            line = ""

            graph = gen_random_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(nodes) + " "

            start_time = time.time()
            bfs(graph, start)
            bfst = (time.time() - start_time)

            line += str(int(round(bfst * 1000))) + " "

            start_time = time.time()
            dfs(graph, start)
            dfst = (time.time() - start_time)

            line += str(int(round(dfst * 1000))) + " "

            # start_time = time.time()
            # bellman_ford(graph, 1)
            # bellman_fordt = (time.time() - start_time)
            #
            # line += str(int(round(bellman_fordt * 1000))) + " "

            start_time = time.time()
            dijkstra_list(graph, start)
            dijkstra_listt = (time.time() - start_time)

            line += str(int(round(dijkstra_listt * 1000))) + " "

            start_time = time.time()
            dijkstra_bh(graph, start)
            dijkstra_bht = (time.time() - start_time)

            line += str(int(round(dijkstra_bht * 1000))) + " "

            start_time = time.time()
            dijkstra_fh(graph, start)
            dijkstra_fht = (time.time() - start_time)

            line += str(int(round(dijkstra_fht * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def exp_topological():
    graph = gen_da_graph(2000, 0.1, 100)

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
    exp_random_graph(0.1, 100)


if __name__ == "__main__":
    main()