import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('test_results/random_g.txt', sep=' ', names=list('nabcde'), index_col=0, header=None)
ns = df.index.values
rep = len(ns[ns == 100])

fig = plt.figure(figsize=(15, 10))

algs = 'abcde'
markers ='.+_x'
colors = 'rgbcm'


plt.subplot(221)
plt.title('Scatter plot')
for a, m, c in zip(algs, markers, colors):
    plt.scatter(ns, df[a], marker=m, color=c, label=a)


plt.subplot(222)
plt.title('Jittered scatter plot')
dev = 0.02 * (max(ns) - min(ns))
devns = ns + np.random.randn(len(ns)) * dev
for a, m, c in zip(algs, markers, colors):
    plt.scatter(devns, df[a], marker=m, color=c, label=a)


plt.subplot(223)
plt.title('Ordered-jittered scatter plot')
step = 6
# devns = ns + np.array(list(range(0, step * rep, step)) * 10)
# for a, m, c in zip(algs, markers, colors):
#     # Series.sort_index(kind='mergesort') -- unexpected keyword argument???
#     s = df.sort_values(a).sort_index(kind='mergesort')
#     plt.scatter(devns, s[a], marker=m, color=c, label=a)


plt.legend(loc='upper left', shadow=True)

plt.show()
