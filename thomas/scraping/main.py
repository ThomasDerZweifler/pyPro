''' 

Scraping parts from https://playmodb.org

Installations:
    pip3 install beautifulsoup4
    pip3 install requests

Starts with:
    python -u "/Users/thomasfunke/git/pyPro/thomas/scraping/main.py"

Info:
    https://playmodb.org/
    https://klicky-ersatzteile.de/

'''

from bs4 import BeautifulSoup
import requests

class Scraper() :

    def __init__(self):
        self.totalParts = 0
        self.klickyContained = 0

    def getTotalParts(self) :
        return self.totalParts

    def getKlickyContained(self) :
        return self.klickyContained

    def getDetailsByPartNumber(self, partNumber):
        pn = partNumber.get_text()
        partnumberUrl = "https://playmodb.org/cgi-bin/showpart.pl?partnum={0}".format(pn)
        print("\n> get {0}".format(partnumberUrl))
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
            self.getDetailsByPartNumber(partNumber)
        
        return self.totalParts


# Problem: setNumber = 7416x

fromSetNumer = 6682
setsCount = 3
toSetNumer = fromSetNumer + setsCount

fromSetNumer = 4000
setsCount = 1
toSetNumer = fromSetNumer + setsCount

totalParts = 0

scraper = Scraper()

for setNumber in range( fromSetNumer, toSetNumer ):
    print("\n> setNumber = {0}".format(setNumber))
    totalParts += scraper.getDetailsBySetNumber(setNumber)

print("\nfrom set number = {0} scraping {1} set(s) and totalParts = {2} (klicky contained: {3})".format(fromSetNumer, toSetNumer-fromSetNumer,totalParts, scraper.getKlickyContained()))

'''

Demo output:

[Running] python -u "/Users/thomasfunke/git/pyPro/thomas/scraping/main.py"

> setNumber = 4000

> get https://playmodb.org/cgi-bin/showpart.pl?partnum=k3201xa
PlaymoDB Part Info for "Man, classic style, brown hair, all blue clothes, fixed wrists"
See Klicky details

> get https://playmodb.org/cgi-bin/showpart.pl?partnum=k3272a
PlaymoDB Part Info for "Man, classic style, blond hair, all blue clothes, fixed wrists"
See Klicky details

> get https://playmodb.org/cgi-bin/showpart.pl?partnum=30 03 7190
PlaymoDB Part Info for "passenger car roof"
Vehicle (Train)

> get https://playmodb.org/cgi-bin/showpart.pl?partnum=30 03 7250
PlaymoDB Part Info for "Caboose platform and rail"
Vehicle (Train)

> get https://playmodb.org/cgi-bin/showpart.pl?partnum=30 03 7270
PlaymoDB Part Info for "Brake handle for train car"
Vehicle (Train)

from set number = 4000 scraping 1 set(s) and totalParts = 5 (klicky contained: 2)

[Done] exited with code=0 in 4.842 seconds

'''
    

