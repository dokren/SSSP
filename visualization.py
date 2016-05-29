import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def visualize_scatter():
    df = pd.read_csv('test_results/bf1_bf2_random_g_100,100,1001.txt', sep=' ', names=list(['n', 'bf1', 'bf2', 'blank']), index_col=0, header=None)
    ns = df.index.values
    rep = 50

    print(df)

    fig = plt.figure(figsize=(15, 10))

    # algs = ['bf1', 'bf2', 'bf3']
    # markers = ['.', '+', 'x']
    # colors = ['r', 'g', 'b']

    algs = ['bf1', 'bf2']
    markers = ['.', '+']
    colors = ['r', 'g']


    # plt.subplot(221)
    plt.title('Bellman-Ford implementations 1 and 2')
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

    df = pd.read_csv('test_results/random_g.txt', sep=' ', names=list('nabcde'), index_col=0, header=None)
    ns = df.index.values


    algs = 'abcde'
    markers ='.+_x.'
    colors = 'rgbcm'


    fig = plt.figure(figsize=(14, 8))

    d = df.groupby(by=df.index.values).median()
    dmin = df.groupby(by=df.index.values).min()
    dmax = df.groupby(by=df.index.values).max()
    davg = (dmax + dmin) / 2
    derr = dmax - davg
    plt.subplot(121)
    plt.title('Error bar')
    for a, m, c in zip(algs, markers, colors):
        plt.errorbar(davg.index.values, davg[a], yerr=derr[a].tolist(), color=c, marker=m, label=a)
        plt.xlim(0, 1100)
    plt.legend(loc='upper left', shadow=True)


    plt.subplot(122)
    plt.title('Boxplot')
    start = {'a': 60, 'b':80, 'c':100, 'd':120, 'e':140}
    for a, m, c in zip(algs, markers, colors):
        bp = df[a].groupby(by=df[a].index).apply(list).tolist()
        pos = range(start[a], 541, 100)
        wds = [15] * 5
        fp = {'color': c}

        plt.boxplot(bp, positions=pos, whis='range', manage_xticks=False, widths=wds, boxprops=fp, medianprops=fp, whiskerprops=fp, capprops=fp)
        plt.xlim(0, 1100)
        plt.xticks(np.arange(100,1001,100))

    plt.show()


def main():
    visualize_scatter()


if __name__ == "__main__":
    main()
