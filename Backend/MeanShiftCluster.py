import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth

from DBConnector import Disease


class MeanShiftCluster:

    def findClusters(self, data):
        PLZ = [o.PLZ for o in data]
        Date = [o.date for o in data]
        Region=[o.Region for o in data]

        #zuordnung = pd.read_csv("./Zuordnung.csv")
        #zuordnung_matrix = zuordnung.get_values().astype(int)

        #plz_array = np.zeros((len(PLZ)), int)
        #for i in range(0, len(PLZ)):
            #if (len(np.argwhere(zuordnung_matrix == PLZ[i])) != 0):
                #plz_array[i] = np.argwhere(zuordnung_matrix == PLZ[i])[0][1] + 1
            #else:
                #print(PLZ[i])
        #region_array = np.zeros((len(PLZ)), int)
        Region =  [int(i * 100000000) for i in Region]
        X = np.array([Region, Date]).T
        bandwidth = estimate_bandwidth(X, quantile=0.082, n_samples=len(X))
        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        ms.fit(X)

        labels = ms.labels_
        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)

        print("number of estimated clusters : %d" % n_clusters_)

        return ms

