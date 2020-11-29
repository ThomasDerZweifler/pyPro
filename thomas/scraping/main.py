''' 

Scraping parts from https://playmodb.org

Installations:
    pip3 install beautifulsoup4
    pip3 install requests
    # pip3 install sqlalchemy

Starts with e.g.:
    python main.py -s 6000 -c 10

    python main.py -s 6000 -c 10 > assciations.csv


append next bulk:
    python main.py -s 7000 -c 10 >> assciations.csv


Info:
    https://playmodb.org/
    https://klicky-ersatzteile.de/


    getOpt:
    https://www.tutorialspoint.com/python/python_command_line_arguments.htm

    logging:
    https://realpython.com/python-logging/

    Html-XML-Scraper:
    http://zetcode.com/python/beautifulsoup/

    Http-Requests:
    https://de.python-requests.org/de/latest/user/quickstart.html

    Database:
    https://docs.sqlalchemy.org/en/13/core/tutorial.html
    https://www.tutorialspoint.com/python_data_persistence/python_data_persistence_sqlalchemy.htm
    https://dbeaver.io

'''
import sys, getopt

# import sqlalchemy
# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
# from sqlalchemy.sql import select

from bs4 import BeautifulSoup
import bs4

# import logging

import requests

# from sql import ScrapingDB

def main(argv):
    logFile = None
    dbFile = None
    fromSetNumber = 0
    setsCount = 0
    try:
        opts, args = getopt.getopt(argv,"hl:d:s:c:",["help","logFile=", "dbFile=","startSet=","setsCount="])
    except getopt.GetoptError:
        print("scraper.py -h -l <name of log file> -d <name of database file> -s <start set number> -c <set count>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("scraper.py -h -l <name of log file> -d <name of database file> -s <start set number> -c <set count>")
            sys.exit()
        elif opt in ("-l", "--logFile"):
            logFile = arg
        elif opt in ("-d", "--dbFile"):
            dbFile = arg
        elif opt in ("-s", "--startSet"):
            fromSetNumber = int(arg, base=10)
        elif opt in ("-c", "--setsCount"):
            setsCount = int(arg, base=10)

    # print("dbFile = {0}; startSet = {1}; setsCount = {2}".format(dbFile, fromSetNumber, setsCount))

    '''

    scrapingDB = ScrapingDB()
    #scrapingDB.create(dbFile=dbFile, logFile=logFile)
    scrapingDB.create()
    scrapingDB.insertAssociation('setName1','partName1')
    scrapingDB.insertAssociation('setName1','partName2')
    scrapingDB.insertAssociation('setName2','partName1')

    scrapingDB.insertAssociation('setName1','partName1')
    scrapingDB.insertAssociation('setName1','partName2')
    scrapingDB.insertAssociation('setName2','partName1')

    result = scrapingDB.selectAllAssociations()

    for row in result:
        print(row)

    print("requests version: {0}".format(requests.__version__))
    print("BeautifulSoup version: {0}".format(bs4.__version__))
    scrapingDB.info()

    '''

    # Problem: setNumber = 7416x
   
    toSetNumer = fromSetNumber + setsCount

    toSetNumer = fromSetNumber + setsCount

    totalParts = 0

    scraper = Scraper()

    for setNumber in range( fromSetNumber, toSetNumer ):
        #print("\n> setNumber = {0}".format(setNumber))
        totalParts += scraper.getDetailsBySetNumber(setNumber)

    #print("\nfrom set number = {0} scraping {1} set(s) and totalParts = {2} (klicky contained: {3})".
    #    format(fromSetNumber, toSetNumer-fromSetNumber,totalParts, scraper.getKlickyContained()))


class Scraper():

    def __init__(self):
        self.totalParts = 0
        self.klickyContained = 0

    def getTotalParts(self) :
        return self.totalParts

    def getKlickyContained(self) :
        return self.klickyContained

    def getDetailsByPartNumber(self, setNumber, partNumber):
        pn = partNumber.get_text()
        partnumberUrl = "https://playmodb.org/cgi-bin/showpart.pl?partnum={0}".format(pn)
        print("\n> get {0}".format(partnumberUrl))

        print("\n setNumber = {0}".format(setNumber))

        detail = requests.get(partnumberUrl)
        soupDetail = BeautifulSoup(detail.content, 'html.parser')
        title = soupDetail.find("title").get_text()
        print(title)

        # https://playmodb.org/cgi-bin/category.pl?cat=Decoration;subcat=Flag

        # first href on page
        category = soupDetail.find('a', href=True).get_text()
        print(category)

        if category == "See Klicky details" :
            self.klickyContained += 1

        self.totalParts += 1
  
    def getPartNumbersBySetNumber(sefl, setNumber):
        page = requests.get("https://playmodb.org/cgi-bin/showinv.pl?setnum={0}".format(setNumber))
        soupPage = BeautifulSoup(page.content, 'html.parser')
        # print(soup.prettify())
        return soupPage.find_all(class_="listpartnumber")

    def getDetailsBySetNumber(self, setNumber):
        partNumbers = Scraper().getPartNumbersBySetNumber(setNumber)
        for partNumber in partNumbers :
            # save to db (assocaition partNUmber to setNumber)

            print("{0};{1}".format(partNumber.get_text(),setNumber))

            # self.getDetailsByPartNumber(setNumber, partNumber)
        
        return self.totalParts

if __name__ == "__main__":
    main(sys.argv[1:])


'''

Demo output:

python main.py -h
scraper.py -h -l <name of log file> -d <name of database file> -s <start set number> -c <set count>

python main.py -help
scraper.py -h -l <name of log file> -d <name of database file> -s <start set number> -c <set count>


python main.py -l app.log -s 100 -c 2
dbFile = ; startSet = 100; setsCount = 2
...


'''
    

