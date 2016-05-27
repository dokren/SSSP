import random


def gen_complete_graph(n, w_range):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            t[j] = random.randrange(1, w_range)
        d[i] = t
    return d


def gen_random_graph(n, prob, w_range):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            if random.random() < prob:
                t[j] = random.randrange(1, w_range)
        d[i] = t
    return d


def gen_net_graph(n, m, w_range):
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


def gen_path_graph(n, w_range):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            t[j] = 1
        d[i] = t
    return d


def gen_da_graph(n, prob, w_range):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(i + 1, n, 1):
            if random.random() < prob:
                t[j] = random.randrange(1, w_range)
        d[i] = t
    return d


def gen_tree_graph(n, w_range):
    d = dict()
    for i in range(n):
        t = dict()
        for j in range(n):
            t[j] = 1
        d[i] = t
    return d
