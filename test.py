from BFS import *
from DFS import *
from Bellman_Ford import *
from Dijkstra import *
from Topological import *
from graph_gen import *


def main():
    # Graph is a dict with vertexes for keys and  dict of edges with weights for values
    test_graph = {1: {2: 1, 3: 1},
                  2: {3: 1, 4: 1},
                  3: {4: 1},
                  4: {},
                  5: {6: 1},
                  6: {3: 1}}

    res1 = bfs(test_graph, 1)
    res2 = dfs(test_graph, 1)
    res3 = bellman_ford(test_graph, 1)
    res4 = dijkstra_list(test_graph, 1)
    res5 = dijkstra_bh(test_graph, 1)
    res6 = dijkstra_fh(test_graph, 1)

    assert res1[0] == res2[0] and res2[0] == res3[0] and res3[0] == res4[0] and res4[0] == res5[0] and res5[0] == res6[0]

    print "Simple test passed!"

    for i in range(100):
        graph = gen_random_graph(50, 0.8, 100)

        start = random.choice(graph.keys())

        res1 = bfs(graph, start)
        res2 = dfs(graph, start)
        res3 = bellman_ford(graph, start)
        res4 = dijkstra_list(graph, start)
        res5 = dijkstra_bh(graph, start)
        res6 = dijkstra_fh(graph, start)

        assert res1[0] == res2[0] and res2[0] == res3[0] and res3[0] == res4[0] and res4[0] == res5[0] and res5[0] == res6[0]

    print "Large random graph test passed!"

    for i in range(100):
        graph = gen_da_graph(10, 0.5, 10)

        start = random.choice(graph.keys())

        resbfs = bfs(graph, start)
        restop = topological(graph, start)

        assert resbfs[0] == restop[0]

    print "Topological test passed!"


if __name__ == "__main__":
    main()