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
    nodes = 400
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
    nodes = 400
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
    f = open('test_results/bf2_dfh_random_g_100,100,1401.txt', 'w+')
    for nodes in range(100, 1401, 100):
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


def exp_bf1(prob, weight_range):
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


def exp_bf2(prob, weight_range):
    f = open('test_results/bf1_bf2_random_g_100,100,1001.txt', 'w+')

    for nodes in range(100, 1001, 100):
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

            f.write("%s\n" % line)

    f.close()


def exp_dijkstra1(prob, weight_range):
    f = open('test_results/dlist_dbhp_dfhp_random_g_100,100,801.txt', 'w+')

    for nodes in range(100, 801, 100):
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


def exp_dijkstra2(prob, weight_range):
    f = open('test_results/dbhp_dfhp_random_g_600,100,1301.txt', 'w+')

    for nodes in range(600, 1301, 100):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_random_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(nodes) + " "

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


def exp_tree_graph(prob, weight_range):
    f = open('test_results/bfs_dfs_bf2_dfh_tree_g_100,100,2001.txt', 'w+')
    for nodes in range(100, 2001, 100):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_tree_graph(nodes, weight_range)

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


def exp_full_graph(prob, weight_range):
    f = open('test_results/bfs_dfs_bf2_dfh_full_g_100,100,501.txt', 'w+')
    for nodes in range(100, 501, 100):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_complete_graph(nodes, weight_range)

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


def exp_net_graph(prob, weight_range):
    f = open('test_results/bfs_dfs_bf2_dfh_net_g_10,5,41.txt', 'w+')
    for nodes in range(10, 36, 5):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_net_graph(nodes, nodes, weight_range)

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


def exp_path_graph(prob, weight_range):
    f = open('test_results/bfs_dfs_bf2_dfh_path_g_1000,1000,10001.txt', 'w+')
    for nodes in range(1000, 10001, 1000):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_path_graph(nodes, weight_range)

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


def exp_topological(prob, weight_range):
    f = open('test_results/t1_t2_random_dag_100,100,801.txt', 'w+')

    for nodes in range(100, 801, 100):
        for i in range(50):
            print "Running for " + str(nodes) + " nodes"
            line = ""

            graph = gen_da_graph(nodes, prob, weight_range)

            start = random.choice(graph.keys())

            line += str(nodes) + " "

            start_time = time.time()
            topological1(graph, start)
            t1 = (time.time() - start_time)

            line += str(int(round(t1 * 1000))) + " "

            start_time = time.time()
            topological2(graph, start)
            t2 = (time.time() - start_time)

            line += str(int(round(t2 * 1000))) + " "

            f.write("%s\n" % line)

    f.close()


def main():
    exp_topological(0.1, 100)
    print "run something"


if __name__ == "__main__":
    main()