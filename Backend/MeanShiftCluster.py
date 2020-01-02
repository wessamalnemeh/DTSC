import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift

from DBConnector import Disease


class MeanShiftCluster:

    def findClusters(self, data):
        PLZ = [o.PLZ for o in data]
        Date = [o.date for o in data]
        X = np.array([PLZ, Date]).T
        ms = MeanShift()
        ms.fit(X)
        return ms

