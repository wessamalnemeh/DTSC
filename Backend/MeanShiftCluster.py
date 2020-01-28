import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth

from DBConnector import Disease


class MeanShiftCluster:

    def findClusters(self, data):
        PLZ = [o.PLZ for o in data]
        Date = [int(o.date) for o in data]
        Region=[o.Region for o in data]
        Lat=[o.lat for o in data]
        Lng=[o.lng for o in data]


       # Region =  [int(i * 100000000) for i in Region]
       # X = np.array([Region, Date]).T
       # bandwidth = estimate_bandwidth(X, quantile=0.082, n_samples=len(X))
       # ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
       # ms.fit(X)

        X = np.array([Lat,Lng, Date]).T
        bandwidth = estimate_bandwidth(X, quantile=0.1, n_samples=len(X))
        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        ms.fit(X)
        labels = ms.labels_
        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)

        print("number of estimated clusters : %d" % n_clusters_)

        return ms

