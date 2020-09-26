# Mongo DB : https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
# PythonMongo: https://www.w3schools.com/python/python_mongodb_getstarted.asp

# mySQL DB: https://dev.mysql.com/downloads/mysql/
# PythonMySQL: https://www.w3schools.com/python/python_mysql_getstarted.asp

# pip install mysql-connector-python

import sys, mysql.connector

# Connector für MySQL installieren --> in Terminal eingeben
# C:\Users\gerri\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\python.exe -m pip install mysql-connector-python
 
# Server starten
# 'services.msc' in commandline --> MySQLGerriet starten

config = {
  'host':'localhost',
  'user':'thomas',
  'password':'Tester#3'
  #'database':'sys'
}

try:
    connection = mysql.connector.connect(host="localhost", user="root",passwd="Tester#3",db="sys")
    # connection = mysql.connector.connect(**config)

    # connection = mysql.connector.connect(host='localhost', user='thomas',passwd='Tester#3')

    print("Verbindung hergestellt")
except:
    print("Keine Verbindung zum Server.")
 
print(connection)

mycursor = connection.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# cursor = connection.cursor()
 
# cursor.execute("SELECT city.Name FROM country INNER JOIN city ON country.capital = city.id WHERE country.Name ='Aruba' ;")
# result = cursor.fetchone()
# print(result)
 
mycursor.close()
connection.close()