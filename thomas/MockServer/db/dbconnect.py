import sys, mysql.connector
import json

# Connector für MySQL installieren --> in Terminal eingeben
# C:\Users\gerri\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe -m pip install mysql-connector-python
 
# Server starten
# 'services.msc' in commandline --> MySQLGerriet starten
class Database() :

    def getConnection(self) :

        connection = None
        try:
            connection = mysql.connector.connect(host="localhost", user="root",passwd="Tester#3",db="mock")
            print("Connection to mock db successfully established.")
        except:
            print("None connection to mock db established.")

        return connection

    # delete path by given EP_path, if EP_path == None delete all endpoints 
    def deletePath(self, EP_path) :

        connection = self.getConnection()
        if(connection == None) : return

        cursor = connection.cursor()

        print("mysql cursor: {0}".format(cursor))

        query = "DELETE FROM endpoints WHERE EP_path = '{0}'".format(EP_path)

        if(EP_path == None) : 
            query = "DELETE FROM endpoints"

        print("mysql query: {0}".format(query))

        try:
            cursor.execute(query)
            connection.commit()
            print("---> mysql query executed: {0}".format(query))
            print(cursor.rowcount, "record inserted.")
        except Exception as e:
            print("---> mysql query execution fails: {0}".format(e))            

        if (cursor):
            cursor.close()
            print("mysql cursor is closed")
        
        if (connection):
            connection.close()
            print("mysql connection is closed")

        return None

    def addResponseForPath(self, EP_description, EP_flavor, EP_method, EP_path, EP_json) :

        result = None

        connection = self.getConnection()
        if(connection == None) : return

        cursor = connection.cursor()

        print("mysql cursor: {0}".format(cursor))

        query = "INSERT INTO endpoints (EP_creation, EP_description, EP_flavor, EP_method, EP_path, EP_json) \
            VALUES (NOW(), '{0}', '{1}', '{2}', '{3}', '{4}')".format(EP_description, EP_flavor, EP_method, EP_path, EP_json) #ON DUPLICATE KEY UPDATE EP_path = 'EP_path'

        print("mysql query: {0}".format(query))

        try:
            cursor.execute(query)
            connection.commit()
            print("---> mysql query executed: {0}".format(query))
            print(cursor.rowcount, "record inserted.")
            result = query
        except Exception as e:
            print("---> mysql query execution fails: {0}".format(e))            

        if (cursor):
            cursor.close()
            print("mysql cursor is closed")
        
        if (connection):
            connection.close()
            print("mysql connection is closed")

        return result

    def searchBy(self, path, method):
        items = []
        uuid = 0

        connection = self.getConnection()
        if(connection == None) : return items

        cursor = connection.cursor()

        where = "WHERE EP_path = '{0}'".format(path)

        query = "SELECT * FROM endpoints {0}".format(where)

        print("mysql query: {0}".format(query))

        cursor.execute(query)
        print("---> mysql query executed: {0}".format(query))
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
                print("creation: ", row[7])
                print("-------------")
                uuid += 1
                an_item = dict(logo="swagger_logo.png", timestamp=row[1], creation=row[7], id=str(uuid), flavor=row[3],
                    description=row[2], method=row[4], path=row[5], response=response)
                items.append(an_item)

        if (cursor):
            cursor.close()
            print("mysql cursor is closed")
        
        if (connection):
            connection.close()
            print("mysql connection is closed")

        return items

    def getAllPaths(self) :
        items = []
        uuid = 0

        connection = self.getConnection()
        if(connection == None) : return items

        cursor = connection.cursor()

        print("mysql cursor: {0}".format(cursor))

        query = "SELECT * FROM endpoints"

        print("mysql query: {0}".format(query))

        cursor.execute(query)
        print("---> mysql query executed: {0}".format(query))
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
                print("creation: ", row[7])
                print("-------------")
                uuid += 1
                an_item = dict(logo="swagger_logo.png", timestamp=row[1], creation=row[7], id=str(uuid), flavor=row[3],
                    description=row[2], method=row[4], path=row[5], response=row[6])
                items.append(an_item)

        if (cursor):
            cursor.close()
            print("mysql cursor is closed")
        
        if (connection):
            connection.close()
            print("mysql connection is closed")

        return items

    def getResponseForPath(self, EP_path) :

        response = None

        connection = self.getConnection()
        if(connection == None) : return response

        cursor = connection.cursor()

        print("mysql cursor: {0}".format(cursor))

        query = "SELECT * FROM endpoints WHERE EP_path = '{0}'".format(EP_path)

        print("mysql query: {0}".format(query))

        cursor.execute(query)
        print("---> mysql query executed: {0}".format(query))
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
                print("creation: ", row[7])
                print("-------------")

        if (cursor):
            cursor.close()
            print("mysql cursor is closed")
        
        if (connection):
            connection.close()
            print("mysql connection is closed")

        return response 

    def test(self) :

        result = self.addResponseForPath('a description', 'a flavor', 'GET', 'path_eight', '{result: {"key1":"value1"}{"key2":"value2"}')

        if result != None:
            print("path_eight sucessfully inserted")
        else : 
            print("path_eight not inserted")

        result = self.addResponseForPath('a description', 'a flavor', 'GET', 'path_five', '{result: {"key1":"value1"}{"key2":"value2"}')

        if result != None:
            print("path_five sucessfully inserted")
        else : 
            print("path_five not inserted")

        path = 'path_five'
        response = self.getResponseForPath(path)
        if response != None:
            print("response for {0} is: {1}".format(path, response.decode("utf-8")))
        else : 
            print("none response exists for {0}".format(path))

        # self.deletePath(path)

        response = self.getResponseForPath(path)
        if response != None:
            print("response for {0} is: {1}".format(path, response.decode("utf-8")))
        else : 
            print("none response exists for {0}".format(path))


Database().test()