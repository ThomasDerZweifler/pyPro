import sys, mysql.connector

# Connector für MySQL installieren --> in Terminal eingeben
# C:\Users\gerri\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe -m pip install mysql-connector-python
 
# Server starten
# 'services.msc' in commandline --> MySQLGerriet starten
class Database() :

    def addResponseForPath(self, EP_description, EP_flavor, EP_method, EP_path, EP_json) :

        connection = None
        try:
            connection = mysql.connector.connect(host="localhost", user="root",passwd="Tester#3",db="mock")
            print("Connection to mock db successfully established.")
        except:
            print("None connection to mock db established.")
        
        print(connection)

        cursor = connection.cursor()

        print("mysql cursor: {0}".format(cursor))

        query = "INSERT INTO endpoints (EP_timestamp,EP_description,EP_flavor,EP_method,EP_path,EP_json) \
            VALUES (now(),'{0}','{1}','{2}','{3}','{4}')".format(EP_description, EP_flavor, EP_method, EP_path, EP_json) #ON DUPLICATE KEY UPDATE EP_path = 'EP_path'

        print("mysql query: {0}".format(query))

        try:
            cursor.execute(query)
            connection.commit()
            print("mysql query executed: {0}".format(query))
            print(cursor.rowcount, "record inserted.")
        except Exception as e:
            print("mysql query execution fails: {0}".format(e))            

        if (cursor):
            cursor.close()
            print("mysql cursor is closed")
        
        if (connection):
            connection.close()
            print("mysql connection is closed")


    def getResponseForPath(self, EP_path) :

        response = None

        connection = None
        try:
            connection = mysql.connector.connect(host="localhost", user="root",passwd="Tester#3",db="mock")
            print("Connection to mock db successfully established.")
        except:
            print("None connection to mock db established.")
        
        print(connection)

        cursor = connection.cursor()

        print("mysql cursor: {0}".format(cursor))

        query = "SELECT * FROM endpoints WHERE EP_path = '{0}'".format(EP_path)

        print("mysql query: {0}".format(query))

        cursor.execute(query)
        records = cursor.fetchall()

        if(records != None) :

            print("Total rows are:  ", len(records))
            for row in records:
                print("Id: ", row[0])
                print("timestamp: ", row[1])
                print("description: ", row[2])
                print("flavor: ", row[3])
                print("method: ", row[4])
                print("path: ", row[5])
                print("response: ", row[6])
                response = row[6]
                print("type response: {0}".format(type(response)))
                print("-------------")

        if (cursor):
            cursor.close()
            print("mysql cursor is closed")
        
        if (connection):
            connection.close()
            print("mysql connection is closed")

        return response 

    def test(self) :

        self.addResponseForPath('a description', 'a flavor', 'GET', 'path_eight', '{result: {"key1":"value1"}{"key2":"value2"}')

        path = 'path_five'
        response = self.getResponseForPath(path)
        if response != None:
            print("response for {0} is: {1}".format(path, response.decode("utf-8")))
        else : 
            print("none response exists for {0}".format(path))


Database().test()