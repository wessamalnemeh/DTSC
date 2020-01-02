import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D




def main():
    data = pd.read_csv("./Niereninsuffizienz.csv")
    X=np.array([data.PLZ,data.Datum]).T
    #clusters = [[1, 1, 1], [5, 5, 5], [3, 10, 10]]
    #X, _ = make_blobs(n_samples=150, centers=clusters, cluster_std=0.60)

    ms = MeanShift()
    ms.fit(X)
    cluster_centers = ms.cluster_centers_


    #fig = plt.figure()
    index=0
    for label in  ms.labels_:
        if label==0:
            color='r'
        else:
            color='b'
        plt.scatter(X[index:, 0], X[index:, 1], marker='o',color=color)
        index+=1

    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='green')
    plt.show()
    print("Done")


if __name__ == "__main__":
    main()
