import decimal
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
            return {'Date':obj.date,'PLZ':obj.PLZ}
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

@route('/api/dieases')
def hello():
    diease_name=request.query.diease
    area=request.query.area
    #Query data from Database
    connector=DBConnector()
    dieases_list=connector.getEventsByDiaeses(diease_name,area)
    #Build Clusters
    meanShift=MeanShiftCluster()
    ms:MeanShift=meanShift.findClusters(dieases_list)
    #Build json response
    response=[]
    for i in range(ms.cluster_centers_.shape[1]):
        idx_list=np.where(ms.labels_==i)
        cluster={}
        cluster["cluster_id"]=i
        cluster["elements"] =np.array(dieases_list)[idx_list]
        response.append(cluster)
    return json.dumps(response,cls=MyEncoder)

run(host='localhost', port=8082, debug=True)