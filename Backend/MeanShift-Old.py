import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth, KMeans
from sklearn.datasets.samples_generator import make_blobs
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
from itertools import cycle

from DBConnector import DBConnector


def main():
    connector = DBConnector()
    dieases_list = connector.getEventsByDiaeses("schnupfen", "Berlin")

    PLZ = [o.PLZ for o in dieases_list]
    Date = [int(o.date) for o in dieases_list]
    Region = [o.Region for o in dieases_list]
    Lat = [o.lat for o in dieases_list]
    Lng = [o.lng for o in dieases_list]



    X = np.array([Lat, Lng, Date]).T
    bandwidth = estimate_bandwidth(X, quantile=0.082, n_samples=len(X))
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    #ms = KMeans(n_clusters=12)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]
        ax.scatter(X[my_members, 0], X[my_members, 1], X[my_members, 2], c=col, marker='o')
        #plt.plot(X[my_members, 0], X[my_members, 1], X[my_members, 2],col + , c=c, marker='o''.')
        #ax.scatter3D(X[my_members, 0], X[my_members, 1], X[my_members, 2], c=col);
        #ax.plot(cluster_center[0], cluster_center[1], cluster_center[2], 'o', markerfacecolor=col,
                 #markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()


if __name__ == "__main__":
    main()
