import mysql.connector as mysql
from geopy.geocoders import OpenMapQuest
import time
import pandas as pd
import numpy as np

class Disease:
    def __init__(self,date,PLZ,Region,lat,lng):
        self.date=date
        self.PLZ = PLZ
        self.Region=Region
        self.lat=lat
        self.lng = lng


    def getDate(self):
        return  self.date

    def getPLZ(self):
        return  self.PLZ

    def getRegion(self):
        return self.Region

    def getLat(self):
        return  self.lat

    def getLng(self):
        return  self.lng


class DBConnector:

    def __init__(self):
        self.db = mysql.connect(
        host='localhost',
        database='tier_db',
        user='root',
        password='password'
        )

    def getEventsByDiaeses(self,diease_name,area):
        cursor =self.db.cursor()
        cursor.execute("SELECT  * FROM tier_db.tier_view2 where tier_view2.diagnose like '%"+diease_name+"%' and ort = '"+area+"' and lat is not null group by TierNr")
        records = cursor.fetchall()
        diseases_list=[]
        zuordnung = pd.read_csv("./Zuordnung.csv")
        zuordnung_matrix = zuordnung.get_values().astype(int)
        for row in records:
            if len(np.argwhere(zuordnung_matrix == int(row[8]))):
                region= np.argwhere(zuordnung_matrix == int(row[8]))[0][1] + 1
                disease=Disease(row[5],int(row[8]),int(region),row[10],row[11])
                diseases_list.append(disease)
            else:
                print(int(row[8]))

        return diseases_list


    def insertLatLangDB(self):

        cursor = self.db.cursor()
        cursor.execute("SELECT  * FROM tier_db.tier_view where tier_view.diagnose like '%niereninsuffizienz%' and ort = 'Berlin' group by TierNr")
        records = cursor.fetchall()
        geolocator = OpenMapQuest(api_key="XFxbqwthDaTnze70Q77fQ0XwatHUyW4p")
        f = open("locations.sql", "w")
        for row in records:
            if(row[7]!=None and row[8]!=None and row[9]!=None):
                address=row[7]+", "+row[8]+" "+row[9].split("(")[0]
                location = geolocator.geocode(address,timeout=None)
                if(location is not None):
                    print(row[1],(location.latitude, location.longitude))
                    query="INSERT INTO `tier_db`.`gplocations`(`adrsId`,`lat`,`lng`) VALUES("+str(row[1])+","+str(location.latitude)+","+str(location.longitude)+");\n"
                    f.write(query)
                else:
                    error="#Failed:"+str(row[1])+"\n"
                    f.write(error)

        f.close()



        print("Bye")


