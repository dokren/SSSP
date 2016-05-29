import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def visualize_scatter():
    df = pd.read_csv('test_results/bfs_bf2_d-fheap_t2_random_dag_100,200,2001.txt', sep=' ', names=list(['n', 'bfs', 'bf2', 'd-fheap', 't2', 'blank']), index_col=0, header=None)
    ns = df.index.values
    rep = 50


    fig = plt.figure(figsize=(15, 10))

    # algs = ['bf1', 'bf2', 'bf3']
    # markers = ['.', '+', 'x']
    # colors = ['r', 'g', 'b']

    algs = ['bfs', 'bf2', 'd-fheap', 't2']
    markers = ['.', '+', 'x', '_']
    colors = ['r', 'g', 'b', 'c']


    # plt.subplot(221)
    plt.title('Topological search implementation 2 with other algorithms')
    plt.xlabel('# nodes')
    plt.ylabel('Time [ms]')
    dev = 0.02 * (max(ns) - min(ns))
    devns = ns + np.random.randn(len(ns)) * dev
    d = df.groupby(by=df.index).mean()
    for a, m, c in zip(algs, markers, colors):
        plt.scatter(devns, df[a], marker=m, color=c, label=a)
        plt.plot(d.index, d[a], color=c, label=a)


    # plt.subplot(222)
    # plt.title('Jittered scatter plot')
    # dev = 0.02 * (max(ns) - min(ns))
    # devns = ns + np.random.randn(len(ns)) * dev
    # for a, m, c in zip(algs, markers, colors):
    #     plt.scatter(devns, df[a], marker=m, color=c, label=a)
    #
    #
    # plt.subplot(223)
    # plt.title('Ordered-jittered scatter plot')
    # step = 2
    # devns = ns + np.array(list(range(0, step * rep, step)) * 6)
    # for a, m, c in zip(algs, markers, colors):
    #     # Series.sort_index(kind='mergesort') -- unexpected keyword argument???
    #     s = df.sort_values(a).sort_index(kind='mergesort')
    #     plt.scatter(devns, s[a], marker=m, color=c, label=a)


    plt.legend(loc='upper left', shadow=True)

    plt.show()


def visualize_box():

    df = pd.read_csv('test_results/bfs_bf2_d-fheap_t2_random_dag_100,200,2001.txt', sep=' ', names=list(['n', 'bfs', 'bf2', 'd-fheap', 't2', 'blank']), index_col=0, header=None)
    ns = df.index.values


    algs = ['bfs', 'bf2', 'd-fheap', 't2']
    markers = ['.', '+', 'x', '_']
    colors = ['r', 'g', 'b', 'c']

    fig = plt.figure(figsize=(15, 10))

    plt.title('Topological search implementation 2 with other algorithms')
    plt.xlabel('# nodes')
    plt.ylabel('Time [ms]')

    d = df.groupby(by=df.index.values).median()
    dmin = df.groupby(by=df.index.values).min()
    dmax = df.groupby(by=df.index.values).max()
    davg = (dmax + dmin) / 2
    derr = dmax - davg

    start = {'bfs': 40, 'bf2':80, 'd-fheap':120, 't2':160}
    for a, m, c in zip(algs, markers, colors):
        bp = df[a].groupby(by=df[a].index).apply(list).tolist()
        pos = range(start[a], 2001, 200)
        wds = [20] * 10
        fp = {'color': c}

        plt.boxplot(bp, positions=pos, whis='range', manage_xticks=False, widths=wds, boxprops=fp, medianprops=fp, whiskerprops=fp, capprops=fp)
        plt.xlim(-100, 2050)
        plt.ylim(-100, 500)
        plt.xticks(np.arange(100, 2000, 200))

    plt.legend(loc='upper left', shadow=True)

    plt.show()


def main():
    visualize_box()
    visualize_scatter()


if __name__ == "__main__":
    main()
