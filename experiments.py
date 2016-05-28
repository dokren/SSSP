import random
from BFS import *
from DFS import *
from Bellman_Ford import *
from Dijkstra import *
from Topological import *
from graph_gen import *
import time


def exp_random_graph4(proba, weight_range):
    f = open('test_results/bfs_dfs_bf2_dfh_random_g_400nodes_0.1,0.1,1.txt', 'w+')
    nodes = 200
    for num in range(1, 11, 1):
        prob = float(num)/10
        for i in range(50):
            print "Running for " + str(prob) + " prob"
            line = ""

            graph = gen_random_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(prob) + " "

            start_time = time.time()
            bfs(graph, start)
            bfst = (time.time() - start_time)

            line += str(int(round(bfst * 1000))) + " "

            start_time = time.time()
            dfs(graph, start)
            dfst = (time.time() - start_time)

            line += str(int(round(dfst * 1000))) + " "

            start_time = time.time()
            bellman_ford2(graph, 1)
            bellman_fordt2 = (time.time() - start_time)
            line += str(int(round(bellman_fordt2 * 1000))) + " "

            start_time = time.time()
            dijkstra_fh(graph, start)
            dijkstra_fht = (time.time() - start_time)

            line += str(int(round(dijkstra_fht * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def exp_random_graph3(prob, wr):
    f = open('test_results/bfs_dfs_bf2_dfh_random_g_400nodes_10,100,1011.txt', 'w+')
    nodes = 200
    for weight_range in range(10, 1011, 100):
        for i in range(50):
            print "Running for " + str(weight_range) + " weight_range"
            line = ""

            graph = gen_random_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(weight_range) + " "

            start_time = time.time()
            bfs(graph, start)
            bfst = (time.time() - start_time)

            line += str(int(round(bfst * 1000))) + " "

            start_time = time.time()
            dfs(graph, start)
            dfst = (time.time() - start_time)

            line += str(int(round(dfst * 1000))) + " "

            start_time = time.time()
            bellman_ford2(graph, 1)
            bellman_fordt2 = (time.time() - start_time)
            line += str(int(round(bellman_fordt2 * 1000))) + " "

            start_time = time.time()
            dijkstra_fh(graph, start)
            dijkstra_fht = (time.time() - start_time)

            line += str(int(round(dijkstra_fht * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def exp_random_graph2(prob, weight_range):
    f = open('test_results/bf2_dfh_random_g_100,100,1001.txt', 'w+')
    for nodes in range(100, 1001, 100):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_random_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(nodes) + " "

            start_time = time.time()
            bellman_ford2(graph, 1)
            bellman_fordt2 = (time.time() - start_time)
            line += str(int(round(bellman_fordt2 * 1000))) + " "

            start_time = time.time()
            dijkstra_fh(graph, start)
            dijkstra_fht = (time.time() - start_time)

            line += str(int(round(dijkstra_fht * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def exp_random_graph1(prob, weight_range):
    f = open('test_results/bfs_dfs_bf2_dfh_random_g_100,50,500.txt', 'w+')
    for nodes in range(100, 501, 50):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
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

            start_time = time.time()
            bellman_ford2(graph, 1)
            bellman_fordt2 = (time.time() - start_time)
            line += str(int(round(bellman_fordt2 * 1000))) + " "

            start_time = time.time()
            dijkstra_fh(graph, start)
            dijkstra_fht = (time.time() - start_time)

            line += str(int(round(dijkstra_fht * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def exp_topological():
    graph = gen_da_graph(1000, 0.5, 100)

    start = random.choice(graph.keys())

    print "bfs:"
    start_time = time.time()
    bfs(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "dfs:"
    start_time = time.time()
    dfs(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "dijkstra_bheap:"
    start_time = time.time()
    dijkstra_bh(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "topological:"
    start_time = time.time()
    topological(graph, start)
    print("--- %s seconds ---" % (time.time() - start_time))


def exp_bf(prob, weight_range):
    f = open('test_results/bf1_bf2_bf3_random_g_100,50,351.txt', 'w+')

    for nodes in range(100, 351, 50):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_random_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(nodes) + " "

            start_time = time.time()
            bellman_ford1(graph, start)
            bfst = (time.time() - start_time)

            line += str(int(round(bfst * 1000))) + " "

            start_time = time.time()
            bellman_ford2(graph, start)
            dfst = (time.time() - start_time)

            line += str(int(round(dfst * 1000))) + " "

            start_time = time.time()
            bellman_ford3(graph, 1)
            bellman_fordt2 = (time.time() - start_time)
            line += str(int(round(bellman_fordt2 * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def exp_dijkstra(prob, weight_range):
    f = open('test_results/dlist_dbhp_dfhp_random_g_100,50,500.txt', 'w+')

    for nodes in range(100, 501, 50):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_random_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(nodes) + " "

            start_time = time.time()
            dijkstra_list(graph, start)
            bfst = (time.time() - start_time)

            line += str(int(round(bfst * 1000))) + " "

            start_time = time.time()
            dijkstra_bh(graph, start)
            dfst = (time.time() - start_time)

            line += str(int(round(dfst * 1000))) + " "

            start_time = time.time()
            dijkstra_fh(graph, 1)
            bellman_fordt2 = (time.time() - start_time)
            line += str(int(round(bellman_fordt2 * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def main():
    print "run something"


if __name__ == "__main__":
    main()