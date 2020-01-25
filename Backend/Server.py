import decimal
from operator import attrgetter

from bottle import route, run ,request, response, template
import numpy as np
from DBConnector import DBConnector, Disease
from MeanShiftCluster import MeanShiftCluster
from sklearn.cluster import MeanShift
import json

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, Disease):
            return {'Date':obj.date,'PLZ':obj.PLZ,'Region':obj.Region,'Lat':obj.lat,'Lng':obj.lng}
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


@route('/api/build')
def buildLocationsTable():
    connector = DBConnector()
    connector.insertLatLangDB()

@route('/api/diseases')
def getDieasesByClusters():
    diease_name=request.query.disease
    area=request.query.area
    #Query data from Database
    connector=DBConnector()
    dieases_list=connector.getEventsByDiaeses(diease_name,area)
    #Build Clusters
    meanShift=MeanShiftCluster()
    ms:MeanShift=meanShift.findClusters(dieases_list)
    #Build json response
    response=[]
    for i in range(ms.cluster_centers_.shape[0]):
        idx_list=np.where(ms.labels_==i)
        cluster={}
        cluster["cluster_id"]=i
        cluster["cluster_low_space"]=min(np.array(dieases_list)[idx_list], key=attrgetter('PLZ')).PLZ
        cluster["cluster_high_space"] = max(np.array(dieases_list)[idx_list], key=attrgetter('PLZ')).PLZ
        cluster["cluster_low_time"] = min(np.array(dieases_list)[idx_list], key=attrgetter('date')).date
        cluster["cluster_high_time"] = max(np.array(dieases_list)[idx_list], key=attrgetter('date')).date
        cluster["elements"] =np.array(dieases_list)[idx_list]
        obj= min(np.array(dieases_list)[idx_list], key=attrgetter('PLZ'))
        response.append(cluster)
    return json.dumps(response,cls=MyEncoder)

run(host='localhost', port=8082, debug=True)