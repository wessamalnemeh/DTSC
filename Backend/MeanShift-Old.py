import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth, KMeans
from sklearn.datasets.samples_generator import make_blobs
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from itertools import cycle



def main():
    data = pd.read_csv("./Niereninsuffizienz.csv")
    zuordnung=pd.read_csv("./Zuordnung.csv")
    zuordnung_matrix=zuordnung.get_values().astype(int)

    plz_array=np.zeros((len(data.PLZ)),int)
    for i in range(0,len(data.PLZ)):
        if(len(np.argwhere(zuordnung_matrix==data.PLZ[i]))!=0):
            plz_array[i]=np.argwhere(zuordnung_matrix==data.PLZ[i])[0][1]+1
        else:
            print(data.PLZ[i])


    normalized_data=data.PLZ*100000
    plz_array=plz_array*100000000
    X=np.array([data.Datum,plz_array]).T

    centers = [[1, 1], [-1, -1], [1, -1]]
    #X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)

    bandwidth = estimate_bandwidth(X, quantile=0.075, n_samples=len(X))

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    #ms = KMeans(n_clusters=12)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)


    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()


if __name__ == "__main__":
    main()
