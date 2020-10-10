import sys, mysql.connector

# Connector für MySQL installieren --> in Terminal eingeben
# C:\Users\gerri\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe -m pip install mysql-connector-python
 
# Server starten
# 'services.msc' in commandline --> MySQLGerriet starten
class Database() :

    def getCapital(self, aCountry) :

        capital = "unknown"

        connection = None
        try:
            connection = mysql.connector.connect(host="localhost", user="root",passwd="Tester#3",db="world")
            print("Verbindung hergestellt")
        except:
            print("Keine Verbindung zum Server.")
        
        print(connection)

        cursor = connection.cursor()

        print(cursor)

        cursor.execute("SELECT city.Name FROM country INNER JOIN city ON country.capital = city.id WHERE country.Name ='{0}' ;".format(aCountry))
        result = cursor.fetchone()

        if(result != None) :

            print(result)

            capital = result[0]

        cursor.close()
        connection.close()

        return capital

    def test() :
        country = "German"
        result = Database().getCapital(country)
        print("the capital of {0} is {1}.".format(country,result))