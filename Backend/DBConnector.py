import mysql.connector as mysql


class Disease:
    def __init__(self,date,PLZ):
        self.PLZ=PLZ
        self.date=date

    def getPLZ(self):
        return  self.PLZ

    def getDate(self):
        return  self.date

class DBConnector:

    def __init__(self):
        self.db=db = mysql.connect(
        host='localhost',
        database='tier_db',
        user='root',
        password='password'
        )

    def getEventsByDiaeses(self,diease_name,area):
        cursor =self.db.cursor()
        cursor.execute("SELECT  * FROM tier_db.tier_view where tier_view.diagnose like '%"+diease_name+"%' and ort = '"+area+"' group by TierNr")
        records = cursor.fetchall()
        diseases_list=[]
        for row in records:
            disease=Disease(row[5],row[8])
            diseases_list.append(disease)
        return diseases_list
