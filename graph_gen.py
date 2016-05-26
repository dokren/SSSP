import random


def gen_complete_graph(n):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            t[j] = random.randrange(1, 20)
        d[i] = t
    return d


def gen_random_graph(n, prob):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            if random.random() < prob:
                t[j] = random.randrange(1, 200)
        d[i] = t
    return d


def gen_net_graph(n, m):
    d = dict()
    for i in range(n):
        for j in range(m):
            t = dict()
            t[((i + 1) % n, j)] = 1
            t[(i, (j + 1) % m)] = 1
            t[((i - 1) % n, j)] = 1
            t[(i, (j - 1) % m)] = 1

            d[(i, j)] = t
    return d


def gen_bipartite_graph(n, m):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            t[j] = 1
        d[i] = t
    return d


def gen_path_graph(n):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            t[j] = 1
        d[i] = t
    return d


def gen_tree_graph(n):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            t[j] = 1
        d[i] = t
    return d
